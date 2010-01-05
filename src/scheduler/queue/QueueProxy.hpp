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

#ifndef WNS_SCHEDULER_QUEUE_QUEUEPROXY_HPP
#define WNS_SCHEDULER_QUEUE_QUEUEPROXY_HPP

#include <WNS/scheduler/queue/QueueInterface.hpp>
#include <WNS/scheduler/queue/IQueueManager.hpp>
#include <WNS/scheduler/SchedulerTypes.hpp>
#include <queue>


namespace wns { namespace scheduler { namespace queue {

        /** @brief This virtual queue is intended to be used by a Master UL scheduler
            and passes all calls to the according queue of the Slave UL scheduler(s) in the UT(s). 
            A system specific QueueManager must be available mapping CIDs to according Queues.*/

        class QueueProxy :
            public wns::scheduler::queue::QueueInterface
            {
            public:
                QueueProxy(wns::ldk::HasReceptorInterface*, const wns::pyconfig::View& config);
                virtual ~QueueProxy();

                bool 
                isAccepting(const wns::ldk::CompoundPtr& compound) const;

                /** @brief compound in */
                void 
                put(const wns::ldk::CompoundPtr& compound);

                wns::scheduler::UserSet 
                getQueuedUsers() const;

                wns::scheduler::ConnectionSet 
                getActiveConnections() const;

                uint32_t 
                numCompoundsForCid(wns::scheduler::ConnectionID cid) const;

                uint32_t 
                numBitsForCid(wns::scheduler::ConnectionID cid) const;

                wns::scheduler::QueueStatusContainer 
                getQueueStatus() const;

                /** @brief compound out */
                wns::ldk::CompoundPtr 
                getHeadOfLinePDU(wns::scheduler::ConnectionID cid);

                int 
                getHeadOfLinePDUbits(wns::scheduler::ConnectionID cid);

                bool 
                isEmpty() const;

                bool 
                hasQueue(wns::scheduler::ConnectionID cid);

                bool 
                queueHasPDUs(wns::scheduler::ConnectionID cid);

                wns::scheduler::ConnectionSet 
                filterQueuedCids(wns::scheduler::ConnectionSet connections);

                void 
                setColleagues(wns::scheduler::RegistryProxyInterface* _registry);

                /** @brief needed for probes */
                void 
                setFUN(wns::ldk::fun::FUN* fun);

                std::string 
                printAllQueues();

                wns::scheduler::queue::QueueInterface::ProbeOutput 
                resetAllQueues();

                wns::scheduler::queue::QueueInterface::ProbeOutput 
                resetQueues(wns::scheduler::UserID user);

                wns::scheduler::queue::QueueInterface::ProbeOutput 
                resetQueue(wns::scheduler::ConnectionID cid);

                /** @brief true if getHeadOfLinePDUSegment() is supported
                for performance reasons we only check the real queues the first time
                and then save the result. In dbg mode we always check using assures. */
                bool 
                supportsDynamicSegmentation() const;

                /** @brief get compound out and do segmentation into #bits */
                wns::ldk::CompoundPtr 
                getHeadOfLinePDUSegment(wns::scheduler::ConnectionID cid, int bits);

                /** @brief if supportsDynamicSegmentation, this is the minimum size of a segment in bits */
                int 
                getMinimumSegmentSize() const;

            private:
                void
                createQueueCopyIfNeeded(wns::scheduler::ConnectionID cid);

                struct Colleagues {
                    wns::scheduler::RegistryProxyInterface* registry_;
                    wns::scheduler::queue::IQueueManager* queueManager_;
                } colleagues;

                std::string queueManagerServiceName_;
                bool readOnly_;
                std::map<wns::scheduler::ConnectionID, wns::simulator::Time> lastChecked_;
                std::map<wns::scheduler::ConnectionID, std::queue<wns::ldk::CompoundPtr> > copyQueue_; 
 
                wns::logger::Logger logger_;
                wns::ldk::fun::FUN* myFUN_;
            };
        }}} // namespace wns::scheduler::queue
#endif // WNS_SCHEDULER_QUEUE_QUEUEPROXY_HPP
