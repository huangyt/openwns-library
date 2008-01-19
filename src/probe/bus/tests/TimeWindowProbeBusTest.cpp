/******************************************************************************
 * WNS (Wireless Network Simulator)                                           *
 * __________________________________________________________________________ *
 *                                                                            *
 * Copyright (C) 2004-2006                                                    *
 * Chair of Communication Networks (ComNets)                                  *
 * Kopernikusstr. 16, D-52074 Aachen, Germany                                 *
 * phone: ++49-241-80-27910 (phone), fax: ++49-241-80-22242                   *
 * email: wns@comnets.rwth-aachen.de                                          *
 * www: http://wns.comnets.rwth-aachen.de                                     *
 ******************************************************************************/

#include <WNS/TestFixture.hpp>
#include <WNS/simulator/ISimulator.hpp>

#include <WNS/probe/bus/TimeWindowProbeBus.hpp>
#include <WNS/probe/bus/tests/ProbeBusStub.hpp>
#include <WNS/pyconfig/Parser.hpp>

#include <sstream>

namespace wns { namespace probe { namespace bus { namespace tests {

    class TimeWindowProbeBusTest:
        public wns::TestFixture
    {
        CPPUNIT_TEST_SUITE( TimeWindowProbeBusTest );
        CPPUNIT_TEST( testNotAttached );
        CPPUNIT_TEST( testAttached );
        CPPUNIT_TEST( testDetached );
        CPPUNIT_TEST_SUITE_END();

    public:
        void prepare();
        void cleanup();

        void testNotAttached();
        void testAttached();
        void testDetached();

    private:
        ProbeBusStub* master;
        ProbeBus* testee;
        ProbeBusStub* listener;

    };
} // tests
} // bus
} // probe
} // wns

using namespace wns::probe::bus::tests;

CPPUNIT_TEST_SUITE_REGISTRATION( TimeWindowProbeBusTest );

void
TimeWindowProbeBusTest::prepare()
{
    std::string config = "import openwns.ProbeBus\n"
        "timewindow = openwns.ProbeBus.TimeWindowProbeBus(start=0.1, end=100.12)\n";
    wns::pyconfig::Parser p;
    p.loadString(config);
    master = new ProbeBusStub();
    testee = new TimeWindowProbeBus(p.get<wns::pyconfig::View>("timewindow"));
    listener = new ProbeBusStub();
    // This is delayed by the TimeWindowProbeBus
    testee->startReceiving(master);
    // The listener immediately connects to the testee
    listener->startReceiving(testee);
}

void
TimeWindowProbeBusTest::cleanup()
{
    delete master;
    delete testee;
    delete listener;
}

void
TimeWindowProbeBusTest::testNotAttached()
{
    wns::probe::bus::Context reg;
    master->forwardMeasurement(0.001, 1.345, reg);
    // No time has passed, we should not be attached
    CPPUNIT_ASSERT(listener->receivedCounter == 0);
}

void
TimeWindowProbeBusTest::testAttached()
{
    wns::probe::bus::Context reg;

    master->forwardMeasurement(0.001, 6.325, reg);
    // No time has passed, we should not be attached
    CPPUNIT_ASSERT(listener->receivedCounter == 0);

    CPPUNIT_ASSERT(wns::simulator::getEventScheduler()->processOneEvent());

    CPPUNIT_ASSERT(wns::simulator::getEventScheduler()->getTime() == 0.1);
    master->forwardMeasurement(0.1, 12.998, reg);

    CPPUNIT_ASSERT(listener->receivedCounter == 1);
    CPPUNIT_ASSERT(listener->receivedValues[0] == 12.998);
}

void
TimeWindowProbeBusTest::testDetached()
{
    wns::probe::bus::Context reg;

    master->forwardMeasurement(0.001, 13.13, reg);
    // No time has passed, we should not be attached
    CPPUNIT_ASSERT(listener->receivedCounter == 0);

    CPPUNIT_ASSERT(wns::simulator::getEventScheduler()->processOneEvent());
    CPPUNIT_ASSERT(wns::simulator::getEventScheduler()->processOneEvent());

    CPPUNIT_ASSERT(wns::simulator::getEventScheduler()->getTime() == 100.12);

    master->forwardMeasurement(100.12, 99.0, reg);

    CPPUNIT_ASSERT(listener->receivedCounter == 0);
}
