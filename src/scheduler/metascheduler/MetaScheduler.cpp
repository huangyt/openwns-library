/*******************************************************************************
 * This file is part of openWNS (open Wireless Network Simulator)
 * _____________________________________________________________________________
 *
 * Copyright (C) 2004-2007
 * Chair of Communication Networks (ComNets)
 * Kopernikusstr. 5, D-52074 Aachen, Germany
 * phone: ++49-241-80-27910,
 * fax: ++49-241-80-22242
 * email: info@openwns.org
 * www: http://www.openwns.org
 * _____________________________________________________________________________
 *
 * openWNS is free software; you can redistribute it and/or modify it under the
 * terms of the GNU Lesser General Public License version 2 as published by the
 * Free Software Foundation;
 *
 * openWNS is distributed in the hope that it will be useful, but WITHOUT ANY
 * WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
 * A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 ******************************************************************************/

#include <string>
#include <vector>
#include <string>
#include <functional>
#include <iostream>
#include <fstream>
#include <limits.h>

#include <WNS/scheduler/metascheduler/MetaScheduler.hpp>
#include <WNS/scheduler/strategy/StrategyInterface.hpp>
#include <WNS/scheduler/SchedulerTypes.hpp>
#include <WNS/scheduler/RegistryProxyInterface.hpp>
#include <WNS/scheduler/strategy/Strategy.hpp>

#include <boost/algorithm/string.hpp>

#include <WIMAC/scheduler/Scheduler.hpp>


#include "boost/multi_array.hpp"
#include <cassert>

using namespace wimac::scheduler;
using namespace wns::scheduler::strategy;
using namespace wns::scheduler::metascheduler;

/*
STATIC_FACTORY_REGISTER_WITH_CREATOR(MetaScheduler,
                                     IMetaScheduler,
                                     "RandomMetaScheduler",
                                     wns::PyConfigViewCreator);

*/

void 
UtilityMatrix::createMatrix (int baseStations, std::vector<int>& userTerminalsInBaseStations)
{
  _baseStations = baseStations;
  _userTerminalsInBaseStations = userTerminalsInBaseStations;
  _indexJumpOfBaseStation.clear();
  _indexJumpOfBaseStation.resize (baseStations);
  _data.clear();
  int numberOfElements = 1;
  for (int i=0; i < _baseStations; ++i)
  {
    _indexJumpOfBaseStation[i] = numberOfElements;
    numberOfElements *= _userTerminalsInBaseStations[i];
    
  }
  _data.resize (numberOfElements);
}

void 
UtilityMatrix::setValue (std::vector<int>& userIndices, double value)
{
  int index = 0;
  for (int i=0; i < _baseStations; ++i)
  {
    index += _indexJumpOfBaseStation[i] * userIndices[i];
  }
  _data[index] = value;
  
}

double 
UtilityMatrix::getValue (std::vector<int>& userIndices)
{
  int index = 0;
  for (int i=0; i < _baseStations; ++i)
  {
    index += _indexJumpOfBaseStation[i] * userIndices[i];
  }
  return _data[index];
}

void UtilityMatrix::Print (void)
{
  //only for 2 and 3 BS 
  if (_baseStations < 2)
    return;
  
  if (_baseStations == 2)
  {
    for (int y=0; y < _userTerminalsInBaseStations[1]; ++y)
    {
      for (int x=0; x < _userTerminalsInBaseStations[0]; ++x)
      {
	std::cout << _data[x + y * _indexJumpOfBaseStation[1]] << " ";
      }
      std::cout << std::endl;
    }
  }
  else if (_baseStations == 3)
  {
    for (int z=0; z < _userTerminalsInBaseStations[2]; ++z)
    {
      for (int y=0; y < _userTerminalsInBaseStations[1]; ++y)
      {
	for (int x=0; x < _userTerminalsInBaseStations[0]; ++x)
	{
	  std::cout << _data[x + y * _indexJumpOfBaseStation[1] + z * _indexJumpOfBaseStation[2]] << " ";
	}
	std::cout << std::endl;
      }
      std::cout << std::endl;
      std::cout << std::endl;
    }
  }
  
  std::cout << std::endl;
}



MetaScheduler::MetaScheduler(const wns::pyconfig::View& _config) : 
    IMetaScheduler(),
    defaultCarrier(_config.get<wns::Power>("initialICacheValues.c")),
    defaultInterference(_config.get<wns::Power>("initialICacheValues.i")),
    defaultPathloss(_config.get<wns::Ratio>("initialICacheValues.pl"))
    
    //defaultCarrier(_config.get<wns::Power>("initialICacheValues.c"))
{

}

MetaScheduler::~MetaScheduler () {}


void 
MetaScheduler::attachBS(const wns::pyconfig::View *pyConfig, 
                        wns::scheduler::RegistryProxyInterface* registryProxy,bool IamUplinkMaster)
{
  if(BSMap.find(registryProxy->getMyUserID()) != BSMap.end())
  {
    if(!IamUplinkMaster)
    {
      BSMap.find(registryProxy->getMyUserID())->second->PyConfigDL=pyConfig;
      BSMap.find(registryProxy->getMyUserID())->second->regProxyDL=registryProxy;
    } else {
      BSMap.find(registryProxy->getMyUserID())->second->PyConfigUL=pyConfig;
      BSMap.find(registryProxy->getMyUserID())->second->regProxyUL=registryProxy;
    }
  }else{	    
    if(!IamUplinkMaster)
    {
      BSInfo* tempBS= new BSInfo ;
      tempBS->BSID = registryProxy->getMyUserID();
      tempBS->regProxyDL = registryProxy;
      tempBS->PyConfigDL = pyConfig;
      tempBS->availableFreqChannels = pyConfig->get<int>("freqChannels");
      tempBS->inputDL = NULL;
		
      //0baseStations.push_back (tempBS);
      BSMap.insert(std::make_pair(registryProxy->getMyUserID(), tempBS));
    } else {
      BSInfo* tempBS= new BSInfo ;
      tempBS->BSID = registryProxy->getMyUserID();
      tempBS->regProxyUL = registryProxy;
      tempBS->PyConfigUL = pyConfig;
      tempBS->availableFreqChannels = pyConfig->get<int>("freqChannels");
      tempBS->inputUL = NULL;
			    
      BSMap.insert(std::make_pair(registryProxy->getMyUserID(), tempBS));
      baseStations.push_back (tempBS);
    }			    
  }	  
}

void 
MetaScheduler::attachUT(const wns::pyconfig::View *pyConfig, wns::scheduler::RegistryProxyInterface* registryProxy)
{
  UTInfo* tempUT= new UTInfo ;
  tempUT->UTID = registryProxy->getMyUserID();
  tempUT->PyConfig = pyConfig;
  tempUT->regProxy = registryProxy;
  tempUT->inputUL = NULL;
		    
  UTMap.insert(std::make_pair(registryProxy->getMyUserID(), tempUT));
}
	
void 
MetaScheduler::detach(const std::string &oldScheduler)
{
}

StrategyInput* 
MetaScheduler::returnStrategyInputBS(wns::scheduler::RegistryProxyInterface* registryProxy ,bool IamUplinkMaster)
{
  
  if(BSMap.find(registryProxy->getMyUserID()) != BSMap.end())
  {
    if (IamUplinkMaster)
    {     
      BSInfo* BS = BSMap.find(registryProxy->getMyUserID())->second;
      StrategyInput *p_strategy= new StrategyInput(BS->PyConfigUL->get<int>("freqChannels"), 
						    BS->PyConfigUL->get<double>("slotDuration"), 
						    BS->PyConfigUL->get<int>("numberOfTimeSlots"), 
						    BS->PyConfigUL->get<int>("maxBeams"),
						    metaScheduler
						    ,NULL);
      BS->inputUL = p_strategy;
      return p_strategy;
    }
    else
    {
      BSInfo* BS = BSMap.find(registryProxy->getMyUserID())->second;
      StrategyInput *p_strategy= new StrategyInput(BS->PyConfigDL->get<int>("freqChannels"), 
						    BS->PyConfigDL->get<double>("slotDuration"), 
						    BS->PyConfigDL->get<int>("numberOfTimeSlots"), 
						    BS->PyConfigDL->get<int>("maxBeams"),
						    metaScheduler
						    ,NULL);
      BS->inputDL = p_strategy; 
      return p_strategy;
    }
  }
  else
  {
    return NULL;
  }
}

StrategyInput* 
MetaScheduler::returnStrategyInputUT(wns::scheduler::RegistryProxyInterface* registryProxy)
{
  if(UTMap.find(registryProxy->getMyUserID()) != UTMap.end())
  {
    UTInfo* UT = UTMap.find(registryProxy->getMyUserID())->second;
    StrategyInput *p_strategy= new StrategyInput(UT->PyConfig->get<int>("freqChannels"), 
						  UT->PyConfig->get<double>("slotDuration"), 
						  UT->PyConfig->get<int>("numberOfTimeSlots"), 
						  UT->PyConfig->get<int>("maxBeams"),
						  metaScheduler
						  ,NULL);
    UT->inputUL = p_strategy;
    return p_strategy;
  }
  return NULL;
  
}


void 
MetaScheduler::provideMetaConfiguration(const wns::scheduler::strategy::StrategyInput* strategyInput, 
                                        wns::scheduler::SchedulingMapPtr schedulingMap)
{
   
  mp_StrategyInput = strategyInput;
  mp_schedulingMap = schedulingMap;
  
  int iBaseStations = baseStations.size();
  int iMatrixSize = 1;
  std::vector<int> BaseStationsCounter;
  std::vector<int> BaseStationsSize;
  std::vector<std::vector<int> > currentCombination;
  
  double bestDataRate = 0.0;
  
  // has a schedule been determined
  static bool bComputed = false;
  
  //has the number of transmitting UTs changed
  static bool bChangeInNumberUTs = false;
  
  
  if(!setCurrentBS(strategyInput))
    return;
  
  int frameNr = strategyInput->getFrameNr();
  
  
  //TODO: Separation of MetaScheduler for uplink and downlink
  if(mp_CurrentBSInfo->inputUL == strategyInput)
  {   
    //std::cout<<"###########################################################################"<<std::endl;
    for (int b=0; b < iBaseStations; b++)
    {     
      if (baseStations[b]->inputUL == NULL)
        return;
      
      if (setActiveUserSet (baseStations[b], frameNr))
        bChangeInNumberUTs = true;
      computeRessourceBlockSizes (baseStations[b]);
      
      //std::cout<<baseStations[b]->BSID.getName()<<" "<<baseStations[b]->activeUsers.size()<<std::endl;
    }
    // determine the number of BSs and check if the number of active UTs of each BS have the same size 
    bool bBaseStationIsEmpty = false;
    int  iUserCount = BSMap.begin()->second->activeUsers.size();
    bool bAllBaseStationHaveSameSize = true;
    
    
    for (int b=0; b < baseStations.size(); b++)
    {
      
      if (baseStations[b]->activeUsers.empty())
          bBaseStationIsEmpty = true;
      
      if (iUserCount != baseStations[b]->activeUsers.size())
      {    
        bAllBaseStationHaveSameSize = false;
        
        //TODO: apply Fixed-->future different strategy
        for (int b = 0; b < iBaseStations; b++)
        {
          baseStations[b]->bestCombination.clear();
          if (baseStations[b]->bestCombination.empty())
          {
            for (int i=0; i < baseStations[b]->vActiveUsers.size(); ++i)
            {
              baseStations[b]->bestCombination.push_back(i);
            }
          }
        }
          
        bChangeInNumberUTs = false;
      }
    }
    if (bBaseStationIsEmpty)
    {
      return;
    }
  
  
  // check if an assignment (meta schedule) has already been computed and if the number of UTs changed 
  if (bComputed &&  (!bChangeInNumberUTs))
  {
    //std::cout<<" 1 ";
    //Apply old mapping
    applyMetaSchedule();
    return;
  }
  
  for (int b = 0; b < iBaseStations; b++)
  {
    baseStations[b]->bestCombination.clear();
    if (baseStations[b]->bestCombination.empty())
    {
      for (int i=0; i < baseStations[b]->vActiveUsers.size(); ++i)
      {
        baseStations[b]->bestCombination.push_back(i);
      }
    }
  }
  
  bool bNoDefaultValues = computeInterferenceMap();
  
  
  //TODO: Add strategies for not same size (schedule is only computed if the UTs in all cells is of the same number
  if ((!bNoDefaultValues)||(!bChangeInNumberUTs))
  {
    //Apply default mapping
    applyMetaSchedule();
    return;
  }
  else
  {
    bComputed = true;
    bChangeInNumberUTs = false;
  }
  
  //Setup data
  for (int i = 0; i < iBaseStations; i++)
  {
    std::vector<int> combination;
    int iSize = baseStations[i]->vActiveUsers.size();
    
    BaseStationsSize.push_back(iSize);
    BaseStationsCounter.push_back(0);

    iMatrixSize *= iSize;
  }
  
  throughputMatrix.createMatrix(iBaseStations, BaseStationsSize);
  
  //Setup Matrix
  for (int i=0; i < iMatrixSize; ++i)
  {
    //Walk over matrix
    for (int j=0; j < iBaseStations; ++j)
    {
      BaseStationsCounter[j]++;
      if (BaseStationsCounter[j] == BaseStationsSize[j])
      {
	BaseStationsCounter[j] = 0;
	continue;
      }
      else
	break;
    }
    
    double dValue = 0;
    for (int j=0; j < iBaseStations; ++j)
    {
      std::set<wns::scheduler::UserID> interferer;
      for (int k=0; k < iBaseStations; ++k)
      {
	if (k==j)
	  continue;
	interferer.insert(baseStations[k]->vActiveUsers[BaseStationsCounter[k]]);
      }
      //std::cout << "BS: " << baseStations[j]->name << " Victim: " << baseStations[j]->vActiveUsers[BaseStationsCounter[j]].getName() << " NumberOfInterferer: " << interferer.size() << std::endl;
      dValue += getMaximumThroughputForUser (baseStations[j], baseStations[j]->vActiveUsers[BaseStationsCounter[j]], interferer);
    }
    throughputMatrix.setValue(BaseStationsCounter, dValue);
  }
  
  //std::cout<<"Throughput Matrix:"<<std::endl;
  //throughputMatrix.Print();
  
  BaseStationsCounter.clear();
  BaseStationsCounter.resize(iBaseStations, 0);
  std::vector< std::vector<bool> > ValidIndices (iBaseStations);
  
  ValidIndices.resize(iBaseStations);
  for (int b=0; b < iBaseStations; ++b)
  {
    ValidIndices[b].resize (BaseStationsSize[b], true);
  }
    
    doOptimize();
    applyMetaSchedule();
    
  }
  //TODO
  else if (mp_CurrentBSInfo->inputDL == strategyInput)
  {
    mp_StrategyInput = NULL;
    return;
  }
  else
  {
    mp_StrategyInput = NULL;
    return;
  }
  
}

bool 
MetaScheduler::setCurrentBS(const wns::scheduler::strategy::StrategyInput* strategyInput)
{
  mp_CurrentBSInfo = NULL;
  
  for (int b=0; b < baseStations.size(); ++b)
  {
    if ((baseStations[b]->inputDL==strategyInput)||(baseStations[b]->inputUL==strategyInput))
    {
      mp_CurrentBSInfo = baseStations[b];
      return true;
    } 
  }
  return false;
}


bool
MetaScheduler::setActiveUserSet(BSInfo* p_BSInfo, int frameNr)
{   
  wns::scheduler::UserSet oldActiveUserSet(p_BSInfo->activeUsers);
 
  //if set is already present, clear it and recompute
  if (!p_BSInfo->activeUsers.empty())
  {  
    p_BSInfo->activeUsers.clear();
  }
  
  if (!p_BSInfo->vActiveUsers.empty())
    p_BSInfo->vActiveUsers.clear();
  
  wns::scheduler::ConnectionSet conns;
  for(int prio = 0; prio < p_BSInfo->regProxyUL->getNumberOfPriorities(); prio++)
  {
      wns::scheduler::ConnectionSet c = p_BSInfo->regProxyUL->getConnectionsForPriority (prio);

      wns::scheduler::ConnectionSet::iterator it;
      for(it = c.begin(); it != c.end(); it++)
	  conns.insert(*it);
  }
  
  wns::scheduler::ConnectionSet::iterator it;
  wns::scheduler::UserSet::iterator itUS;
    
  for(it = conns.begin(); it != conns.end(); it++)
  {
    wns::scheduler::UserID user = p_BSInfo->regProxyUL->getUserForCID(*it);
    //Filter out base stations
    if(!user.isBroadcast())
    {
      //Set assumptions does not hold for UserID, so an extra comparision is necessary
      if ( p_BSInfo->activeUsers.find(user) == p_BSInfo->activeUsers.end())
      {
        p_BSInfo->activeUsers.insert(user);
        p_BSInfo->vActiveUsers.push_back(user);
      }
    }
  }
  // TODO: Compare the UserIDs for changes
  if (p_BSInfo->activeUsers.size() == oldActiveUserSet.size())
    return false;
  return true;
   
  
}

void 
MetaScheduler::computeRessourceBlockSizes (BSInfo* p_BSInfo)
{
  p_BSInfo->resourceBlockSizes.clear();
  int numberOfUEs = p_BSInfo->activeUsers.size();
  if (numberOfUEs == 0)
    return;
  
  int numberSubSchannels = p_BSInfo->availableFreqChannels;
  int numberOfLargeTBs = numberSubSchannels % numberOfUEs;
  int LargeTBSize = floor(numberSubSchannels / numberOfUEs) + 1;
  int numberOfSmallTBs = numberOfUEs - numberOfLargeTBs;
  int SmallTBSize = floor(numberSubSchannels / numberOfUEs);
  
  for (int i=0; i<numberOfLargeTBs; ++i)
  {
    p_BSInfo->resourceBlockSizes.push_back(LargeTBSize);
  }
  for (int i=0; i<numberOfSmallTBs; ++i)
  {
    p_BSInfo->resourceBlockSizes.push_back(SmallTBSize);
  }
}



void 
MetaScheduler::applyMetaSchedule (void)
{
  
  updateUserSubchannels();  
  
  for (int b=0; b < baseStations.size(); ++b)
  {
    //Only apply mapping of the current base station
    if (mp_CurrentBSInfo == baseStations[b])
    {
	int frequencies = baseStations[b]->availableFreqChannels;
	//...for each frequency ...
	for (int l=0; l < frequencies; l++)
	{
	  //Reserve user
	  wns::scheduler::UserID user = baseStations[b]->getUserInFrequency (l, baseStations[b]->bestCombination);
	  reservePRB (user, *mp_schedulingMap, l, 0, 0);
	  setPhyModeForPRB (user, *mp_schedulingMap, l, 0, 0);
	}
    }
  }
  
}


void 
MetaScheduler::updateUserSubchannels (void)
{
  
  std::map< int, std::set<int> > mapping;
  
  for (int b=0; b < baseStations.size(); ++b)
  {
    for (int i= 0; i < baseStations[b]->vActiveUsers.size(); i++)
    {
      mapping.insert(std::pair<int, std::set<int> >(baseStations[b]->vActiveUsers[i].getNodeID(), std::set<int>()));
    }
    
    int frequencies = baseStations[b]->availableFreqChannels;
    
    //std::cout<<"availableFreqChannels: "<<baseStations[b]->availableFreqChannels<<std::endl;
    
    for (int l=0; l < frequencies; l++)
    {
      //Reserve user
      
      /*
      std::cout<<"reserve user: "<<l<<" ";
      for (int m=0;m<baseStations[b]->bestCombination.size();m++)
      {
      
        std::cout<<baseStations[b]->bestCombination[m]<<" ";
    
      }
      */
      wns::scheduler::UserID user = baseStations[b]->getUserInFrequency (l, baseStations[b]->bestCombination);
      mapping[user.getNodeID()].insert(l);
    }
  }
  
  //std::cout<<" 5 "<<std::endl;
  
  for (int b=0; b < baseStations.size(); ++b)
  {
    for (int b2=0; b2 < baseStations.size(); ++b2)
    {
      for (int i= 0; i < baseStations[b2]->vActiveUsers.size(); i++)
      {
        //std::cout<<"10"<<std::endl;
        baseStations[b]->regProxyUL->updateUserSubchannels(baseStations[b2]->vActiveUsers[i], 
                                                           mapping[baseStations[b2]->vActiveUsers[i].getNodeID()]);
      }
    }
  }

}

void 
MetaScheduler::setPhyModeForPRB(wns::scheduler::UserID userID, wns::scheduler::SchedulingMap & schedulingMap, 
                                int subChannel, int timeSlot, int spatialLayer)
{
 
  std::set<wns::scheduler::UserID> interferer;
  getInterfererOnFrequency (userID, subChannel, interferer);
  wns::Ratio r = getSINR (mp_CurrentBSInfo, userID, interferer);
    
  //std::cout << "SchedulingMap: " << (long)&schedulingMap << " BS: " << mp_CurrentBSInfo->name << " UserID: " << 
  //userID.getName() << " Interferer: " << interferer.begin()->getName() << " Size:" << interferer.size() << " subChannel: " << subChannel << " SINR: " << r.get_dB()<<"Data Rate: "<<mp_CurrentBSInfo->regProxyUL->getBestPhyMode(r)->getDataRate()<<  "\n";
  //std::cout << "Estimated SIR for: "<<userID.getName()<<" "<<r.get_dB()<<std::endl;
  
  schedulingMap.subChannels[subChannel].temporalResources[timeSlot]->physicalResources[spatialLayer].setPhyMode(mp_CurrentBSInfo->regProxyUL->getBestPhyMode(r));
 
}

void 
MetaScheduler::setPhyModeForPRB(wns::scheduler::UserID userID, wns::scheduler::SchedulingMap & schedulingMap, 
                                int subChannel, int timeSlot, int spatialLayer, wns::service::phy::phymode::PhyModeInterfacePtr pm)
{
 
  //std::cout << "SchedulingMap: " << (long)&schedulingMap << " BS: " << mp_CurrentBSInfo->name << " UserID: " << 
  //userID.getName() << " Interferer: " << interferer.begin()->getName() << " Size:" << interferer.size() << " subChannel: " << subChannel << " SINR: " << r.get_dB()<<"Data Rate: "<<mp_CurrentBSInfo->regProxyUL->getBestPhyMode(r)->getDataRate()<<  "\n";
  //std::cout << "Estimated SIR for: "<<userID.getName()<<" "<<r.get_dB()<<std::endl;
  
  schedulingMap.subChannels[subChannel].temporalResources[timeSlot]->physicalResources[spatialLayer].setPhyMode(pm);

}


bool 
MetaScheduler::computeInterferenceMap (void)
{

  
  bool bNoDefaultValues = true;
  for (int b=0; b < baseStations.size(); b++)
  //for (baseStationContainerIterator itaAB=allBaseStation.begin(); itaAB != allBaseStation.end(); itaAB++)
  {	
   //std::cout<<"-------------------Interference Map-----------------------"<<std::endl; 
   //std::cout << baseStations[b]->BSID.getName() << ": "<<std::endl;
    baseStations[b]->interferenceMap.clear();
    for (int b2=0; b2 < baseStations.size(); b2++)
    {
      
      for (int k=0; k < baseStations[b2]->vActiveUsers.size(); ++k)
      {
	wns::scheduler::UserID  user = baseStations[b2]->vActiveUsers[k];
	wns::scheduler::ChannelQualityOnOneSubChannel q = baseStations[b]->regProxyUL->estimateRxSINROf(user);
	wns::scheduler::ChannelQualityOnOneSubChannel q2 = baseStations[b]->regProxyDL->estimateRxSINROf(user);
	
	if (defaultPathloss.get_dB() == q.pathloss.get_dB())
	  bNoDefaultValues = false;
	if (defaultInterference.get_dBm() == q.interference.get_dBm())
	  bNoDefaultValues = false;
	
	if (q.pathloss.get_dB() == std::numeric_limits<double>::infinity())
	  bNoDefaultValues = false;
	if (q.interference.get_dBm() == std::numeric_limits<double>::infinity())
	  bNoDefaultValues = false;
	if (q.pathloss.get_dB() == -std::numeric_limits<double>::infinity())
	  bNoDefaultValues = false;
	if (q.interference.get_dBm() == -std::numeric_limits<double>::infinity())
	  bNoDefaultValues = false;
	
	if (q.pathloss.get_dB() == std::numeric_limits<double>::quiet_NaN())
	  bNoDefaultValues = false;
	if (q.interference.get_dBm() == std::numeric_limits<double>::quiet_NaN())
	  bNoDefaultValues = false;
	
	
	else if (q.pathloss.get_dB())
		
	baseStations[b]->interferenceMap.insert( 
	  std::pair<int, wns::scheduler::ChannelQualityOnOneSubChannel>(user.getNodeID(), q) );
	
	//if (bNoDefaultValues)
	//{
	 //std::cout << "(" << user.getNodeID() <<" , " <<" P:" << q.pathloss.get_dB() << " C:" << q.carrier.get_dBm() <<" I:"<<q.interference.get_dBm()<<" SIR: "<<(q.carrier/q.interference).get_dB() << ") ";
	 //std::cout << std::endl;
	//}
	
      }
    }
    //std::cout << std::endl;
  }
 // std::cout << std::endl;
  return bNoDefaultValues;
  /**/
}

double 
MetaScheduler::getMaximumThroughputForUser (BSInfo* pBS, wns::scheduler::UserID user, 
                                                   std::set<wns::scheduler::UserID>& interferer)
{
  return pBS->regProxyUL->getBestPhyMode(getSINR (pBS, user, interferer))->getDataRate();
}


 wns::Ratio 
 MetaScheduler::getSINR (BSInfo* pBS, wns::scheduler::UserID user, std::set<wns::scheduler::UserID>& interferer)
 {
  //TODO: fix extimation
  wns::Power interference ;
  interference.set_dBm(-116.440);
  
  for (std::set<wns::scheduler::UserID>::iterator it = interferer.begin(); it != interferer.end(); ++it)
  { 
    interference +=  pBS->interferenceMap[(*it).getNodeID()].carrier;
  }
   wns::Ratio SINR = (pBS->interferenceMap[user.getNodeID()].carrier/interference);
   
   return SINR;
}


void 
MetaScheduler::reservePRB(wns::scheduler::PhysicalResourceBlock *prbDescriptor,wns::scheduler::UserID userID)
{
  prbDescriptor->setUserID(userID);
}


void 
MetaScheduler::reservePRB(wns::scheduler::UserID userID, wns::scheduler::SchedulingMap & schedulingMap, 
                          int subChannel, int timeSlot, int spatialLayer)
{
  schedulingMap.subChannels[subChannel].temporalResources[timeSlot]->physicalResources[spatialLayer].setUserID(userID);

  ////std::cout<<"____________________UserID prescheduled for____________"<<schedulingMap.subChannels[subChannel].temporalResources[timeSlot]->physicalResources[spatialLayer].getMetaUserID().getName();

}


void 
MetaScheduler::getInterfererOnFrequency (BSInfo* pBS, int iFrequency, 
                                         std::vector<std::vector<int> >& currentCombination,
                                         std::set<wns::scheduler::UserID>& interferer)
{
  
  for (int j=0; j<baseStations.size(); j++)
  {
    if (baseStations[j] == pBS)
      continue;
    interferer.insert (baseStations[j]->getUserInFrequency (iFrequency, currentCombination[j]));
  
  }
  /*
  int j=0;
  for (baseStationContainerIterator itaAB=BSMap.begin(); itaAB != BSMap.end(); itaAB++, j++)
  {
    //Don't select interferer for yourself
    if (itaAB->second == pBS)
      continue;
    
    interferer.insert (itaAB->second->getUserInFrequency (iFrequency, currentCombination[j]));    
  }
  */
}

void 
MetaScheduler::getInterfererOnFrequency (wns::scheduler::UserID user, int iFrequency, std::set<wns::scheduler::UserID>& interferer)
{
  for (int b=0; b < baseStations.size(); ++b)
  {
    wns::scheduler::UserID foundUser = baseStations[b]->getUserInFrequency (iFrequency, baseStations[b]->bestCombination);
    if (foundUser.getNodeID() != user.getNodeID())
      interferer.insert (baseStations[b]->getUserInFrequency (iFrequency, baseStations[b]->bestCombination));    
  }
}