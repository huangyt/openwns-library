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

#ifndef WNS_DISTRIBUTION_TEST_LOGNORM_HPP
#define WNS_DISTRIBUTION_TEST_LOGNORM_HPP

#include <WNS/distribution/LogNorm.hpp>

#include <WNS/TestFixture.hpp>

namespace wns { namespace distribution { namespace test {

      class LogNormTest :
    public CppUnit::TestFixture
      {
	CPPUNIT_TEST_SUITE( LogNormTest );
	CPPUNIT_TEST( testIt );
	CPPUNIT_TEST( testVar );
	CPPUNIT_TEST_SUITE_END();
      public:
	void setUp();
	void tearDown();

	void testIt();
	void testVar();

	};

    } // test
  } // distribution
} // wns

#endif // NOT defined WNS_DISTRIBUTION_TEST_LOGNORM_HPP
