/*******************************************************************************
 * This file is part of openWNS (open Wireless Network Simulator)
 * _____________________________________________________________________________
 *
 * Copyright (C) 2004-2009
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

#ifndef WNS_SCHEDULER_STRATEGY_STATICPRIORITY_PERSISTENTVOIP_STATETRACKER_HPP
#define WNS_SCHEDULER_STRATEGY_STATICPRIORITY_PERSISTENTVOIP_STATETRACKER_HPP

#include <WNS/scheduler/SchedulerTypes.hpp>

#include <vector>

namespace wns { namespace scheduler { namespace strategy { namespace staticpriority { namespace persistentvoip {

class StateTracker
{
    public:
        struct ClassifiedConnections :
            public wns::IOutputStreamable
        {
            ConnectionSet newPersistentCIDs;
            ConnectionSet reactivatedPersistentCIDs;
            ConnectionSet persistentCIDs;
            ConnectionSet unpersistentCIDs;
            ConnectionSet silencedCIDs;
        private:
            virtual std::string
            doToString() const;
        };

        StateTracker(unsigned int numberOfFrames, wns::logger::Logger& logger);
        ~StateTracker();
        
        ClassifiedConnections
        updateState(const ConnectionSet& activeCIDs, unsigned int currentFrame);

        void
        silenceCID(ConnectionID cid, unsigned int currentFrame);

    private:
        unsigned int numberOfFrames_;

        std::vector<ConnectionSet> expectedCIDs_;
        std::vector<ConnectionSet> pastPeriodCIDs_;
        ConnectionSet silentCIDs_;
        ConnectionSet allCIDs_;

        wns::logger::Logger* logger_;
};

}}}}}

#endif