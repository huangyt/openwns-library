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

#include "SimpleLinkHandler.hpp"

#include <WNS/ldk/fun/FUN.hpp>
#include <WNS/ldk/FunctionalUnit.hpp>
#include <WNS/ldk/PyConfigCreator.hpp>

#include <WNS/module/Base.hpp>

using namespace wns::ldk;

STATIC_FACTORY_REGISTER_WITH_CREATOR(SimpleLinkHandler,
				     LinkHandlerInterface,
				     "wns.ldk.SimpleLinkHandler",
				     wns::ldk::PyConfigCreator);

SimpleLinkHandler::SimpleLinkHandler(const wns::pyconfig::View& _config) :
	config(_config),
	traceCompoundJourney(config.get<bool>("traceCompoundJourney")),
	isAcceptingLogger(config.get<wns::pyconfig::View>("isAcceptingLogger")),
	sendDataLogger(config.get<wns::pyconfig::View>("sendDataLogger")),
	wakeupLogger(config.get<wns::pyconfig::View>("wakeupLogger")),
	onDataLogger(config.get<wns::pyconfig::View>("onDataLogger"))
{
} // SimpleLinkHandler

bool
SimpleLinkHandler::isAcceptingForwarded(FunctionalUnit* fu, const CompoundPtr& compound)
{
	MESSAGE_BEGIN(VERBOSE, isAcceptingLogger, m, fu->getFUN()->getName());
	m << " calling doIsAccepting of FU "
	  << fu->getName();
	MESSAGE_END();

	bool isAccepting = doIsAccepting(fu, compound);

	MESSAGE_BEGIN(VERBOSE, isAcceptingLogger, m, fu->getFUN()->getName());
	m << " function isAccepting(...) of FU "
	  << fu->getName() << " called: FU is ";
	if (isAccepting)
		m << "accepting";
	else
		m << "not accepting";
	m << "\ncompound: " << compound.getPtr();
	MESSAGE_END();

	return isAccepting;
} // isAcceptingForwarded

void
SimpleLinkHandler::sendDataForwarded(FunctionalUnit* fu, const CompoundPtr& compound)
{
	MESSAGE_BEGIN(VERBOSE, sendDataLogger, m, fu->getFUN()->getName());
	m << " function sendData(...) of FU "
	  << fu->getName() << " called"
	  << "\ncompound: " << compound.getPtr();
	MESSAGE_END();

#ifndef WNS_NO_LOGGING
	if (traceCompoundJourney && compound)
		compound->visit(fu); // JOURNEY
#endif

	doSendData(fu, compound);
} // sendDataForwarded

void
SimpleLinkHandler::wakeupForwarded(FunctionalUnit* fu)
{
	MESSAGE_BEGIN(VERBOSE, wakeupLogger, m, fu->getFUN()->getName());
	m << " function wakeup(...) of FU "
	  << fu->getName() << " called";
	MESSAGE_END();

	doWakeup(fu);
} // wakeupForwarded

void
SimpleLinkHandler::onDataForwarded(FunctionalUnit* fu, const CompoundPtr& compound)
{
	MESSAGE_BEGIN(VERBOSE, onDataLogger, m, fu->getFUN()->getName());
	m << " function onData(...) of FU "
	  << fu->getName() << " called"
	  << "\ncompound: " << compound.getPtr();
	MESSAGE_END();

#ifndef WNS_NO_LOGGING
	if (traceCompoundJourney && compound)
		compound->visit(fu); // JOURNEY
#endif

	doOnData(fu, compound);
} // onDataForwarded


