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

#ifndef WNS_SCHEDULER_STRATEGY_STATICPRIORITY_ROUNDROBIN_HPP
#define WNS_SCHEDULER_STRATEGY_STATICPRIORITY_ROUNDROBIN_HPP

#include <WNS/scheduler/strategy/staticpriority/SubStrategy.hpp>
#include <WNS/scheduler/strategy/Strategy.hpp>
#include <WNS/scheduler/SchedulingMap.hpp>
#include <WNS/scheduler/queue/QueueInterface.hpp>
#include <WNS/scheduler/RegistryProxyInterface.hpp>
#include <WNS/StaticFactory.hpp>

namespace wns { namespace scheduler { namespace strategy { namespace staticpriority {

                /**
                 * @brief Round Robin subscheduler.
                 *
                 */

                class RoundRobin
                        : public SubStrategy
                {
                public:
                    RoundRobin(const wns::pyconfig::View& config);

                    ~RoundRobin();

                    virtual void
                    initialize();

                    /** @brief gives the current cid or the next one, if it doesn't exist anymore */
                    virtual wns::scheduler::ConnectionID
                    getValidCurrentConnection(const ConnectionSet &currentConnections, ConnectionID cid) const;

                    /** @brief gives the next cid to schedule */
                    virtual wns::scheduler::ConnectionID
                    getNextConnection(const ConnectionSet &currentConnections, ConnectionID cid) const;

                    virtual wns::scheduler::MapInfoCollectionPtr
                    doStartSubScheduling(SchedulerStatePtr schedulerState,
                                         wns::scheduler::SchedulingMapPtr schedulingMap);
                protected:
                    /** @brief keep state of RR pointer */
                    wns::scheduler::ConnectionID lastScheduledConnection;
                    /** @brief Number of packets to schedule of the same cid before proceeding to the next one.
                        (PyConfig parameter) */
                    int blockSize;
                };
            }}}}
#endif
