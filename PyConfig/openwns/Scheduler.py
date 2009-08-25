###############################################################################
# This file is part of openWNS (open Wireless Network Simulator)
# _____________________________________________________________________________
#
# Copyright (C) 2004-2007
# Chair of Communication Networks (ComNets)
# Kopernikusstr. 5, D-52074 Aachen, Germany
# phone: ++49-241-80-27910,
# fax: ++49-241-80-22242
# email: info@openwns.org
# www: http://www.openwns.org
# _____________________________________________________________________________
#
# openWNS is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License version 2 as published by the
# Free Software Foundation;
#
# openWNS is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openwns.pyconfig import attrsetter
import openwns.logger
import openwns.scheduler.APCStrategy
import openwns.scheduler.DSAStrategy
import copy

class PowerCapabilities(object):
    maxPerSubband = None
    nominalPerSubband = None
    maxOverall = None

    def __init__(self,
                 maxPerSubband = "0.0 mW",
                 nominalPerSubband = "0.0 mW",
                 maxOverall = "0.0 mW"):
        self.maxPerSubband = maxPerSubband
        self.nominalPerSubband = nominalPerSubband
        self.maxOverall = maxOverall

class Strategy(object):
    nameInStrategyFactory = None
    symbolDuration = None
    txMode = None # True for outgoing schedulers (Scheduler-TX) in BS and UT; False for uplink master scheduler (Scheduler-RX) in BS, because this does not really transmit packets
    logger = None
    powerControlSlave = None # True for slave scheduler in UT
    excludeTooLowSINR = None
    dsastrategy = None
    dsafbstrategy = None
    apcstrategy = None

    def __init__(self,
                 txMode = True,
                 symbolDuration = None,
                 parentLogger = None,
                 powerControlSlave = False,
                 excludeTooLowSINR = True,
                 apcstrategy   = openwns.scheduler.APCStrategy.DoNotUseAPC(),
                 dsastrategy   = openwns.scheduler.DSAStrategy.DoNotUseDSA(),
                 dsafbstrategy = openwns.scheduler.DSAStrategy.DoNotUseDSA(),
                 **kw):
        self.symbolDuration = symbolDuration
        self.txMode = txMode
        self.logger = openwns.logger.Logger("WNS", "Strategy", True, parentLogger)
        self.powerControlSlave = powerControlSlave
        self.excludeTooLowSINR = excludeTooLowSINR
        self.setAPCStrategy(apcstrategy)
        self.setDSAStrategy(dsastrategy)
        self.setDSAFallbackStrategy(dsafbstrategy)
        assert dsafbstrategy.requiresCQI == False, "dsafbstrategy must not require CQI"
        attrsetter(self, kw)
    def setParentLogger(self,parentLogger = None):
        myParentLogger = copy.deepcopy(parentLogger) # original object shares logger instance
        self.logger = openwns.logger.Logger("WNS", "Strategy", True, myParentLogger)
        #self.dsastrategy.setParentLogger(self.logger)
        ### above: BS1.L2.tdd100.RS-TX.Strategy.DSAStrategy.LinearFFirst
        ### below: BS1.L2.tdd100.RS-TX.DSAStrategy.LinearFFirst
        self.dsastrategy.setParentLogger(myParentLogger)
        self.dsafbstrategy.setParentLogger(openwns.logger.Logger("WNS", "FB", True, myParentLogger))
        self.apcstrategy.setParentLogger(myParentLogger)
    def setDSAStrategy(self, dsastrategy):
        self.dsastrategy = copy.deepcopy(dsastrategy)
        self.dsastrategy.setParentLogger(self.logger)
    def setDSAFallbackStrategy(self, dsafbstrategy):
        self.dsafbstrategy = copy.deepcopy(dsafbstrategy)
        self.dsafbstrategy.setParentLogger(self.logger)
    def setAPCStrategy(self, apcstrategy):
        self.apcstrategy = copy.deepcopy(apcstrategy)
        self.apcstrategy.setParentLogger(self.logger)

# The Tx Scheduling Strategies (old style)
class EqualTimeRR(Strategy):

    def __init__(self, **kw):
        super(EqualTimeRR,self).__init__(txMode = True, **kw)
        self.nameInStrategyFactory = "EqualTimeRR"

class ExhaustiveRR(Strategy):

    def __init__(self, powerControlSlave = False, **kw):
        super(ExhaustiveRR,self).__init__(txMode = True, powerControlSlave = powerControlSlave, **kw)
        self.nameInStrategyFactory = "ExhaustiveRR"

class CQIEnabledExhaustiveRR(Strategy):

    useNominalTxPower = None
    useRandomChannelAtBeginning = None

    def __init__(self, useNominalTxPower = True, useRandomChannel = False, **kw):
        super(CQIEnabledExhaustiveRR,self).__init__(txMode = True, **kw)
        self.nameInStrategyFactory = "CQIEnabledExhaustiveRR"
        self.useNominalTxPower = useNominalTxPower
        self.useRandomChannelAtBeginning = useRandomChannel

class ProportionalFairUL(Strategy):
    historyWeight = None
    maxBursts = None
    allowReGrouping = None
    scalingBetweenMaxTPandPFair = None

    def __init__(self, maxBursts, historyWeight=0.9, scalingBetweenMaxTPandPFair=1.0, **kw):
        super(ProportionalFairUL,self).__init__(txMode = False, **kw)
        self.nameInStrategyFactory = "ProportionalFairUL"
        self.historyWeight = historyWeight
        self.scalingBetweenMaxTPandPFair = scalingBetweenMaxTPandPFair
        self.maxBursts = maxBursts
        self.allowReGrouping = False

class ProportionalFairDL(Strategy):
    historyWeight = None # 0.0 = no history; 0.9 = factor of older pastDataRates to keep
    maxBursts = None
    allowReGrouping = None
    scalingBetweenMaxTPandPFair = None # 0.0=MaxThroughput; 1.0=ProportionalFair

    def __init__(self, maxBursts, historyWeight=0.9, scalingBetweenMaxTPandPFair=1.0, **kw):
        super(ProportionalFairDL,self).__init__(txMode = True, **kw)
        self.nameInStrategyFactory = "ProportionalFairDL"
        self.historyWeight = historyWeight
        self.scalingBetweenMaxTPandPFair = scalingBetweenMaxTPandPFair
        self.maxBursts = maxBursts
        self.allowReGrouping = False

class MaxThroughput(ProportionalFairDL):
    """A special version of the PF scheduler"""
    def __init__(self, maxBursts, **kw):
        super(MaxThroughput,self).__init__(historyWeight = 0.0,
                                           maxBursts = maxBursts, **kw)
        self.historyWeight = 0.0
        self.scalingBetweenMaxTPandPFair = 0.0

# The Rx Scheduling Strategies
class CQIEnabledRoundRobinUL(Strategy):
    useNominalTxPower = None
    blockDuration = None
    def __init__(self, txMode = False, _useNominalTxPower = True, **kw):
        super(CQIEnabledRoundRobinUL,self).__init__(txMode = False,**kw)
        self.nameInStrategyFactory = "CQIEnabledRoundRobinUL"
        self.useNominalTxPower = _useNominalTxPower

class RoundRobinUL(Strategy):
    blockDuration = None
    def __init__(self, **kw):
        super(RoundRobinUL,self).__init__(txMode = False, **kw)
        self.nameInStrategyFactory = "RoundRobinUL"

# ResourceRequest aware
class ExhaustiveRRUL(Strategy):
    def __init__(self, powerControlSlave = False, **kw):
        super(ExhaustiveRRUL,self).__init__(txMode = False, powerControlSlave = powerControlSlave, **kw)
        self.nameInStrategyFactory = "ExhaustiveRRUL"

# Power Control (PC) Aware and ResourceRequest (RR) Aware
class PCRR(Strategy):
    blockDuration = None
    def __init__(self, **kw):
        super(PCRR,self).__init__(txMode = False, **kw)
        self.nameInStrategyFactory = "PCRR"

class RelayPreferredRR(Strategy):
    def __init__(self, **kw):
        super(RelayPreferredRR,self).__init__(txMode = False, **kw)
        self.nameInStrategyFactory = "RelayPreferredRR"

######################################################
# QoS enabled (new style)
class StaticPriority(Strategy):
    subStrategies = None
    numberOfPriorities = None
    def __init__(self, txMode = True, subStrategies = [], parentLogger = None, powerControlSlave = False, **kw):
        super(StaticPriority,self).__init__(txMode = txMode, powerControlSlave=powerControlSlave, **kw)
        attrsetter(self, kw)
        self.nameInStrategyFactory = "StaticPriority"
        self.subStrategies = []
        self.logger = openwns.logger.Logger("WNS", "SP", True, parentLogger)
        # priority here is only used for the logger name
        priority = 0
        for subStrategy in subStrategies:
            mySubStrategy = copy.deepcopy(subStrategy) # original object shares logger instance
            logger = openwns.logger.Logger("WNS", "SP[%d]"%priority, True, self.logger)
            mySubStrategy.setParentLogger(logger)
            self.subStrategies.append(mySubStrategy)
            priority = priority+1

class SubStrategy:
    logger = None
    __plugin__ = "NONE"
    def __init__(self, **kw):
        attrsetter(self, kw)
    def setParentLogger(self,parentLogger = None):
        self.logger = openwns.logger.Logger("WNS", "SubStrategy", True, parentLogger)

class RoundRobin(SubStrategy):
    __plugin__ = "RoundRobin"
    blockSize = 1 # number of pdus taken out out queue for one cid per round
    def __init__(self, parentLogger = None, **kw):
        self.logger = openwns.logger.Logger("WNS", "RoundRobin", True, parentLogger)
        attrsetter(self, kw)
    def setParentLogger(self,parentLogger = None):
        self.logger = openwns.logger.Logger("WNS", "RoundRobin", True, parentLogger)

class ExhaustiveRoundRobin(SubStrategy):
    __plugin__ = "ExhaustiveRoundRobin"
    blockSize = 1000000 # don't ask.
    def __init__(self, parentLogger = None, **kw):
        self.logger = openwns.logger.Logger("WNS", "ExhaustiveRR", True, parentLogger)
        attrsetter(self, kw)
    def setParentLogger(self,parentLogger = None):
        self.logger = openwns.logger.Logger("WNS", "ExhaustiveRR", True, parentLogger)

class ProportionalFair(SubStrategy):
    __plugin__ = "ProportionalFair"
    blockSize = 1000000
    # 0.0 = no history; 0.9 = factor of older pastDataRates to keep
    historyWeight = 0.9
    # 0.0=MaxThroughput; 1.0=ProportionalFair
    scalingBetweenMaxTPandPFair = 1.0
    # indicates whether goal is rate (True) or resource (False) fairness
    rateFairness = True
    def __init__(self, parentLogger = None, **kw):
        self.logger = openwns.logger.Logger("WNS", "ProportionalFair", True, parentLogger)
        attrsetter(self, kw)
    def setParentLogger(self,parentLogger = None):
        self.logger = openwns.logger.Logger("WNS", "ProportionalFair", True, parentLogger)

# TODO:
class EqualTimeRoundRobin(SubStrategy):
    __plugin__ = "EqualTimeRoundRobin"
    def __init__(self, parentLogger = None, **kw):
        self.logger = openwns.logger.Logger("WNS", "EqualTimeRR", True, parentLogger)
        attrsetter(self, kw)
    def setParentLogger(self,parentLogger = None):
        self.logger = openwns.logger.Logger("WNS", "EqualTimeRR", True, parentLogger)

# TODO:
class EqualRateRoundRobin(SubStrategy):
    __plugin__ = "EqualRateRoundRobin"
    def __init__(self, parentLogger = None, **kw):
        self.logger = openwns.logger.Logger("WNS", "EqualRateRR", True, parentLogger)
        attrsetter(self, kw)
    def setParentLogger(self,parentLogger = None):
        self.logger = openwns.logger.Logger("WNS", "EqualRateRR", True, parentLogger)

# TODO: First Come First Serve (FCFS)
class FCFS(SubStrategy):
    __plugin__ = "FCFS"
    def __init__(self, parentLogger = None, **kw):
        self.logger = openwns.logger.Logger("WNS", "FCFS", True, parentLogger)
        attrsetter(self, kw)
    def setParentLogger(self,parentLogger = None):
        self.logger = openwns.logger.Logger("WNS", "FCFS", True, parentLogger)

# TODO: Earliest Deadline First (EDF)
class EDF(SubStrategy):
    __plugin__ = "EDF"
    def __init__(self, parentLogger = None, **kw):
        self.logger = openwns.logger.Logger("WNS", "EDF", True, parentLogger)
        attrsetter(self, kw)
    def setParentLogger(self,parentLogger = None):
        self.logger = openwns.logger.Logger("WNS", "EDF", True, parentLogger)


######################################################

class NoGrouper:
    nameInGrouperFactory = "NoGrouper"
    beamforming = False


class Grouper(object):
    nameInGrouperFactory = None
    friendliness_dBm = None
    MonteCarloSim = None
    beamforming = None
    uplink = None
    logger = None

    def __init__(self, parentLogger = None, **kw):
        super(Grouper,self).__init__()
        self.friendliness_dBm = "-95 dBm"
        self.MonteCarloSim = False
        self.beamforming = True
        self.uplink = False
        self.logger = openwns.logger.Logger("WNS", "SpatialGrouper", True, parentLogger);
        attrsetter(self, kw)

class RelayMetaGrouper(Grouper):
    internalStrategy = None
    def __init__(self, internalStrategy, parentLogger = None):
        super(RelayMetaGrouper, self).__init__(parentLogger = parentLogger)
        self.nameInGrouperFactory = 'RelayMetaGrouper'
        self.internalStrategy = internalStrategy

class Treebased(Grouper):
    def __init__(self, **kw):
        super(Treebased,self).__init__(**kw)

class SINRHeuristic(Treebased):
    def __init__(self, **kw):
        super(SINRHeuristic,self).__init__(**kw)
        self.nameInGrouperFactory = "SINRHeuristic"

class DoAGrouper(Treebased):
    minAngleDegree = None
    weight = None
    strategy = None

    def __init__(self, minAngleDegree, weight, **kw):
        super(DoAGrouper,self).__init__(**kw)
        self.minAngleDegree = minAngleDegree
        self.weight = weight
        # Strategy for the cost function
        self.strategy = 0 # 0 means average cost for the group
        #self.strategy = 1 # 1 means cost of group member with maximum cost

class DoAHeuristicLinearCost(DoAGrouper):
    def __init__(self, minAngleDegree, weight, **kw):
        super(DoAHeuristicLinearCost,self).__init__(minAngleDegree, weight, **kw)
        self.nameInGrouperFactory = "DoAHeuristicLinearCost"

class DoAHeuristicPreferredAngle(DoAGrouper):
    def __init__(self, minAngleDegree, weight, **kw):
        super(DoAHeuristicPreferredAngle,self).__init__(minAngleDegree, weight, **kw)
        self.nameInGrouperFactory = "DoAHeuristicPreferredAngle"

class RegistryProxy(object):
    nameInRegistryProxyFactory = None

######################################################
### SimpleQueue (stores segmented PDUs of size<=segmentSize)
class SimpleQueue(object):
    nameInQueueFactory = None
    logger = None
    sizeProbeName = None
    TxRx = None
    localIDs = None

    def setLocalIDs(self, localIDs):
        self.localIDs = localIDs

    def addLocalIDs(self, localIDs):
        self.localIDs.update(localIDs)

    def __init__(self, parentLogger = None, **kw):
        self.localIDs = {}
        self.nameInQueueFactory = "SimpleQueue"
        self.logger = openwns.logger.Logger("WNS", "SimpleQueue", True, parentLogger);
        self.sizeProbeName = 'SimpleQueueSize'
        attrsetter(self, kw)

### SegmentingQueue (stores unsegmented original PDUs and does segmentation on-the-fly)
class SegmentingQueue(object):
    nameInQueueFactory = None
    logger = None
    sizeProbeName = None
    TxRx = None
    localIDs = None
    minimumSegmentSize = None # used to ask for resources of at least this size

    def setLocalIDs(self, localIDs):
        self.localIDs = localIDs

    def addLocalIDs(self, localIDs):
        self.localIDs.update(localIDs)

    def __init__(self, parentLogger = None, **kw):
        super(SegmentingQueue,self).__init__()
        self.localIDs = {}
        self.nameInQueueFactory = "SegmentingQueue"
        self.logger = openwns.logger.Logger("WNS", "SegmentingQueue", True, parentLogger);
        self.sizeProbeName = 'SegmentingQueueSize'
        self.minimumSegmentSize = 32 # Bits
        #self.sizeProbeName = 'schedulerQueueSize'
        attrsetter(self, kw) # new [rs]
