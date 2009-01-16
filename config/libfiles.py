libname = 'wns'
srcFiles = [
    'src/Assure.cpp',
    'src/Birthmark.cpp',
    'src/Direction.cpp',
    'src/Exception.cpp',
    'src/TestFixture.cpp',
    'src/StopWatch.cpp',
    'src/Chamaeleon.cpp',
    'src/IOutputStreamable.cpp',
    'src/PythonicOutput.cpp',
    'src/Backtrace.cpp',
    'src/demangle.cpp',
    'src/Object.cpp',
    'src/Positionable.cpp',

    # module
    'src/module/Base.cpp',
    'src/module/Release.cpp',
    'src/module/DateTime.cpp',
    'src/simulator/IApplication.cpp',
    'src/simulator/Application.cpp',
    'src/simulator/SignalHandler.cpp',
    'src/simulator/SignalHandlerCallback.cpp',
    'src/simulator/AbortHandler.cpp',
    'src/simulator/SegmentationViolationHandler.cpp',
    'src/simulator/InterruptHandler.cpp',
    'src/simulator/CPUTimeExhaustedHandler.cpp',
    'src/simulator/ISimulator.cpp',
    'src/simulator/Simulator.cpp',
    'src/simulator/UnitTests.cpp',
    'src/simulator/ISimulationModel.cpp',
    'src/simulator/StatusReport.cpp',
    'src/simulator/ProbeWriter.cpp',
    'src/simulator/OutputPreparation.cpp',
    'src/pyconfig/Object.cpp',
    'src/pyconfig/View.cpp',
    'src/pyconfig/Parser.cpp',
    'src/pyconfig/Sequence.cpp',
    'src/pyconfig/helper/Functions.cpp',
    'src/events/scheduler/IEvent.cpp',
    'src/events/scheduler/Interface.cpp',
    'src/events/scheduler/CommandQueue.cpp',
    'src/events/scheduler/Map.cpp',
    'src/events/scheduler/INotification.cpp',
    'src/events/scheduler/Monitor.cpp',
    'src/events/scheduler/RealTime.cpp',
    'src/events/CanTimeout.cpp',
    'src/events/PeriodicTimeout.cpp',
    'src/events/PeriodicRealTimeout.cpp',
    'src/events/tests/MultipleTimeoutTest.cpp',


    'src/evaluation/statistics/stateval.cpp',
    'src/evaluation/statistics/moments.cpp',
    'src/evaluation/statistics/pdf.cpp',

    'src/logger/Master.cpp',
    'src/logger/Message.cpp',
    'src/logger/Logger.cpp',
    'src/logger/OutputStrategy.cpp',
    'src/logger/CoutOutput.cpp',
    'src/logger/CerrOutput.cpp',
    'src/logger/FileOutput.cpp',
    'src/logger/ConsoleFormat.cpp',
    'src/logger/XMLFormat.cpp',
    'src/logger/DelimiterFormat.cpp',
    'src/logger/SQLiteFormat.cpp',
    'src/logger/FormatStrategy.cpp',
    
    'src/probe/bus/Context.cpp',
    'src/probe/bus/ContextFilterProbeBus.cpp',
    'src/probe/bus/ContextProvider.cpp',
    'src/probe/bus/ContextCollector.cpp',
    'src/probe/bus/LoggingProbeBus.cpp',
    'src/probe/bus/TimeSeriesProbeBus.cpp',
    'src/probe/bus/PassThroughProbeBus.cpp',
    'src/probe/bus/ProbeBus.cpp',
    'src/probe/bus/ProbeBusRegistry.cpp',
    'src/probe/bus/PythonProbeBus.cpp',
    'src/probe/bus/SettlingTimeGuardProbeBus.cpp',
    'src/probe/bus/StatEvalProbeBus.cpp',
    'src/probe/bus/TableProbeBus.cpp',
    'src/probe/bus/TextProbeBus.cpp',
    'src/probe/bus/TimeWindowProbeBus.cpp',
    'src/probe/bus/detail/ObserverPimpl.cpp',
    'src/probe/bus/detail/OutputFormatter.cpp',
    'src/probe/bus/detail/SubjectPimpl.cpp',
    'src/probe/bus/detail/Sorter.cpp',
    'src/probe/bus/detail/StatEvalTable.cpp',
    'src/probe/bus/utils.cpp',

    'src/testing/DetailedListener.cpp',
    'src/testing/TestTool.cpp',
    
    'src/osi/PDU.cpp',
    'src/osi/PCI.cpp',

    'src/node/Node.cpp',
    'src/node/NodeSimulationModel.cpp',
    'src/node/component/Component.cpp',
    'src/node/component/FQSN.cpp',

    'src/service/tl/PortPool.cpp',

    'src/distribution/Fixed.cpp',
    'src/distribution/NegExp.cpp',
    'src/distribution/Norm.cpp',
    'src/distribution/Uniform.cpp',
    'src/distribution/DiscreteUniform.cpp',
    'src/distribution/Pareto.cpp',
    'src/distribution/Binomial.cpp',
    'src/distribution/Geometric.cpp',
    'src/distribution/Erlang.cpp',
    'src/distribution/Poisson.cpp',
    'src/distribution/CDFTable.cpp',
    'src/distribution/TimeDependent.cpp',
    'src/distribution/Operation.cpp',
    'src/distribution/Rice.cpp',

    'src/queuingsystem/Job.cpp',
    'src/queuingsystem/JobContextProvider.cpp',
    'src/queuingsystem/MM1Step1.cpp',
    'src/queuingsystem/MM1Step2.cpp',
    'src/queuingsystem/MM1Step3.cpp',
    'src/queuingsystem/MM1Step5.cpp',
    'src/queuingsystem/MM1Step6.cpp',
    'src/queuingsystem/GGn.cpp',
    'src/queuingsystem/Server.cpp',

    'src/tests/AverageTest.cpp',
    'src/tests/AssureTest.cpp',
    'src/tests/ChamaeleonTest.cpp',
    'src/tests/ExceptionTest.cpp',
    'src/tests/TypeInfoTest.cpp',
    'src/tests/FunctorTest.cpp',
    'src/tests/StaticFactoryTest.cpp',
    'src/tests/SmartPtrTest.cpp',
    'src/tests/SmartPtrWithDebuggingTest.cpp',
    'src/tests/PythonicOutputTest.cpp',
    'src/tests/StopWatchTest.cpp',
    'src/tests/BacktraceTest.cpp',
    'src/tests/ObserverTest.cpp',
    'src/tests/ObjectTest.cpp',
    'src/tests/IntervalTest.cpp',
    'src/tests/EnumeratorTest.cpp',
    'src/tests/BirthmarkTest.cpp',
    'src/tests/BrokerTest.cpp',
    'src/tests/CacheTest.cpp',
    'src/tests/ClassTest.cpp',
    'src/tests/CloneableTest.cpp',
    'src/tests/DerefLessTest.cpp',
    'src/tests/DirectionTest.cpp',
    'src/tests/DoubleDispatcherTest.cpp',
    'src/tests/EnumTest.cpp',
    'src/tests/NearestNeighbourTest.cpp',
    'src/tests/NLinearTest.cpp',
    'src/tests/PositionableTest.cpp',
    'src/tests/PowerRatioTest.cpp',
    'src/tests/CandITest.cpp',
    'src/tests/RoundRobinTest.cpp',
    'src/tests/SlidingWindowTest.cpp',
    'src/tests/StaticFactoryBrokerTest.cpp',
    'src/tests/TimeWeightedAverageTest.cpp',
    'src/tests/WeightedAverageTest.cpp',
    'src/tests/TypeTraitsTest.cpp',

    'src/module/tests/ModuleTest.cpp',
    'src/module/tests/MultiTypeFactoryTest.cpp',
    'src/simulator/tests/MainTest.cpp',
    'src/container/tests/FastListTest.cpp',
    'src/container/tests/UntypedRegistryTest.cpp',
    'src/container/tests/RegistryTest.cpp',
    'src/container/tests/DynamicMatrixTest.cpp',
    'src/container/tests/PoolTest.cpp',
    'src/container/tests/RangeMapTest.cpp',
    'src/container/tests/MatrixTest.cpp',

    'src/pyconfig/tests/ParserTest.cpp',
    'src/pyconfig/tests/ViewTest.cpp',
    'src/pyconfig/tests/SequenceTest.cpp',
    'src/pyconfig/helper/tests/FunctionsTest.cpp',
    'src/logger/tests/MasterTest.cpp',
    'src/logger/tests/MessageTest.cpp',
    'src/logger/tests/LoggerTest.cpp',
    'src/logger/tests/LoggerTestHelper.cpp',
    'src/probe/bus/tests/ContextTest.cpp',
    'src/probe/bus/tests/ContextFilterProbeBusTest.cpp',
    'src/probe/bus/tests/ContextProviderTest.cpp',
    'src/probe/bus/tests/ContextProviderCollectionTest.cpp',
    'src/probe/bus/tests/PassThroughProbeBusTest.cpp',
    'src/probe/bus/tests/ProbeBusRegistryTest.cpp',
    'src/probe/bus/tests/ProbeBusStub.cpp',
    'src/probe/bus/tests/PythonProbeBusTest.cpp',
    'src/probe/bus/tests/TimeWindowProbeBusTest.cpp',
    'src/probe/bus/tests/TableProbeBusTest.cpp',
    'src/probe/bus/tests/DevelopersGuideTest.cpp',
    'src/probe/bus/tests/DevelopersGuideTestCollector.cpp',
    'src/probe/bus/detail/tests/SorterTest.cpp',

    'src/evaluation/statistics/tests/StatEvalTest.cpp',

    'src/events/tests/MemberFunctionTest.cpp',
    'src/events/tests/DelayedMemberFunctionTest.cpp',
    'src/events/scheduler/tests/CallableTest.cpp',
    'src/events/scheduler/tests/InterfaceTest.cpp',
    'src/events/scheduler/tests/MapInterfaceTest.cpp',
    'src/events/scheduler/tests/PerformanceTest.cpp',
    'src/events/scheduler/tests/MapPerformanceTest.cpp',
    'src/events/scheduler/tests/BestPracticesTest.cpp',
    'src/events/scheduler/tests/RealTimeTest.cpp',
    'src/events/tests/CanTimeoutTest.cpp',
    'src/events/tests/PeriodicTimeoutTest.cpp',
    'src/events/tests/PeriodicRealTimeoutTest.cpp',

    'src/osi/tests/PCITest.cpp',
    'src/osi/tests/PDUTest.cpp',

    'src/service/nl/tests/Address.cpp',

    'src/node/tests/NodeTest.cpp',
    'src/node/tests/NodeHeaderReaderTest.cpp',
    'src/node/tests/Stub.cpp',   
    'src/node/component/tests/ComponentStub.cpp',
    'src/node/component/tests/ComponentTest.cpp',
    'src/node/component/tests/IP.cpp',
    'src/node/component/tests/TCP.cpp',
    'src/node/component/tests/FQSNTest.cpp',

    'src/service/dll/Address.cpp',
    'src/service/dll/ProtocolNumber.cpp',
    'src/service/tl/tests/PortPoolTest.cpp',
    'src/service/phy/phymode/SNR2MIInterface.cpp',
    'src/service/phy/phymode/MI2PERInterface.cpp',
    'src/service/phy/phymode/PhyModeMapperInterface.cpp',

    'src/distribution/tests/FixedTest.cpp',
    'src/distribution/tests/VarEstimator.cpp',
    'src/distribution/tests/NegExpTest.cpp',
    'src/distribution/tests/ErlangTest.cpp',
    'src/distribution/tests/NormTest.cpp',
    'src/distribution/tests/UniformTest.cpp',
    'src/distribution/tests/DiscreteUniformTest.cpp',
    'src/distribution/tests/PoissonTest.cpp',
    'src/distribution/tests/GeometricTest.cpp',
    'src/distribution/tests/ParetoTest.cpp',
    'src/distribution/tests/BinomialTest.cpp',
    'src/distribution/tests/CDFTableTest.cpp',
    'src/distribution/tests/RiceTest.cpp',
    'src/distribution/tests/TimeDependentTest.cpp',
    'src/distribution/tests/OperationTest.cpp',
    
    'src/geometry/Point.cpp',
    'src/geometry/Vector.cpp',
    'src/geometry/Shape2D.cpp',
    'src/geometry/AABoundingBox.cpp',
    'src/geometry/LineSegment.cpp',
    'src/geometry/AxisParallelRectangle.cpp',
    'src/geometry/tests/PointTest.cpp',
    'src/geometry/tests/VectorTest.cpp',
    'src/geometry/tests/LineSegmentTest.cpp',
    'src/geometry/tests/AABoundingBoxTest.cpp',
    'src/geometry/tests/AxisParallelRectangleTest.cpp',
    
    'src/markovchain/tests/MarkovBaseTest.cpp',
    'src/markovchain/tests/MarkovDiscreteTimeTest.cpp',
    'src/markovchain/tests/MarkovContinuousTimeTest.cpp',
    'src/markovchain/tests/MarkovContinuousTimeTrafficTest.cpp',
    'src/markovchain/tests/MarkovDiscreteTimeTrafficTest.cpp',
    
    # ldk
    'src/ldk/FunctionalUnit.cpp',
    'src/ldk/CommandTypeSpecifier.cpp',
    'src/ldk/Compound.cpp',
    'src/ldk/CommandPool.cpp',
    'src/ldk/CommandProxy.cpp',
    'src/ldk/RandomAccessLink.cpp',
    'src/ldk/SingleLink.cpp',
    'src/ldk/SingleReceptor.cpp',
    'src/ldk/SingleConnector.cpp',
    'src/ldk/SingleDeliverer.cpp',
    'src/ldk/MultiLink.cpp',
    'src/ldk/FirstServeConnector.cpp',
    'src/ldk/RoundRobinLink.cpp',
    'src/ldk/RoundRobinReceptor.cpp',
    'src/ldk/RoundRobinConnector.cpp',
    'src/ldk/RoundRobinDeliverer.cpp',
    'src/ldk/FlowSeparator.cpp',
    'src/ldk/FlowGate.cpp',
    'src/ldk/Group.cpp',
    'src/ldk/SequentlyCallingLinkHandler.cpp',
    'src/ldk/SimpleLinkHandler.cpp',
    'src/ldk/SuspendSupport.cpp',
    'src/ldk/ManagementServiceInterface.cpp',
    'src/ldk/ControlServiceInterface.cpp',

    'src/ldk/fun/Main.cpp',
    'src/ldk/fun/Sub.cpp',

    'src/ldk/utils.cpp',

    # ldk.Buffer
    'src/ldk/buffer/Buffer.cpp',
    'src/ldk/buffer/Bounded.cpp',
    'src/ldk/buffer/Dropping.cpp',

    # ldk.ARQ
    'src/ldk/arq/None.cpp',
    'src/ldk/arq/StopAndWait.cpp',
    'src/ldk/arq/CumulativeACK.cpp',
    'src/ldk/arq/SelectiveRepeat.cpp',
    'src/ldk/arq/GoBackN.cpp',
    'src/ldk/arq/PiggyBacker.cpp',
    'src/ldk/arq/statuscollector/None.cpp',
    'src/ldk/arq/statuscollector/Counter.cpp',
    'src/ldk/arq/statuscollector/TwoSizesWindowed.cpp',

    # ldk.CRC
    'src/ldk/crc/CRC.cpp',
    'src/ldk/crc/CRCFilter.cpp',

    # ldk.SAR
    'src/ldk/sar/Fixed.cpp',
    'src/ldk/sar/Soft.cpp',

    # ldk.Concatenation
    'src/ldk/concatenation/Concatenation.cpp',

    # ldk.Tools
    'src/ldk/tools/Synchronizer.cpp',
    'src/ldk/tools/Bridge.cpp',
    'src/ldk/tools/Stub.cpp',
    'src/ldk/tools/PERProviderStub.cpp',
    'src/ldk/tools/Forwarder.cpp',
    'src/ldk/tools/Padding.cpp',
    'src/ldk/tools/Gate.cpp',
    'src/ldk/tools/Stutter.cpp',
    'src/ldk/tools/BottleNeckDetective.cpp',
    'src/ldk/tools/Overhead.cpp',
    'src/ldk/tools/Consumer.cpp',
    'src/ldk/tools/ConstantDelay.cpp',

    # ldk.Probe
    'src/ldk/probe/Packet.cpp',
    'src/ldk/probe/Window.cpp',
    'src/ldk/probe/ErrorRate.cpp',
    'src/ldk/probe/bus/Packet.cpp',
    'src/ldk/probe/bus/Window.cpp',

    # ldk.Command
    'src/ldk/command/FlowControl.cpp',

    # ldk.Multiplexer
    'src/ldk/multiplexer/Dispatcher.cpp',
    'src/ldk/multiplexer/FrameDispatcher.cpp',
    'src/ldk/multiplexer/OpcodeProvider.cpp',
    'src/ldk/multiplexer/OpcodeDeliverer.cpp',
    'src/ldk/multiplexer/OpcodeSetter.cpp',
    'src/ldk/multiplexer/OpcodeKey.cpp',

    # ldk.FrameConfigurationFramework
    'src/ldk/fcf/FrameBuilder.cpp',
    'src/ldk/fcf/PhaseDescriptor.cpp',
    'src/ldk/fcf/TimingControl.cpp',
    'src/ldk/fcf/NewFrameProviderObserver.cpp',

    # ldk.FlowSeparator
    'src/ldk/flowseparator/NotFoundStrategy.cpp',
    'src/ldk/flowseparator/CreatorStrategy.cpp',


    'src/ldk/tests/LayerTest.cpp',
    'src/ldk/tests/LayerStub.cpp',
    'src/ldk/tests/FunctionalUnitTest.cpp',
    'src/ldk/tests/RoundRobinLinkTest.cpp',
    'src/ldk/tests/RandomAccessLinkTest.cpp',
    'src/ldk/tests/SingleLinkTest.cpp',
    'src/ldk/tests/SingleReceptorTest.cpp',
    'src/ldk/tests/SingleConnectorTest.cpp',
    'src/ldk/tests/SingleDelivererTest.cpp',
    'src/ldk/tests/MultiLinkTest.cpp',
    'src/ldk/tests/FirstServeConnectorTest.cpp',
    'src/ldk/tests/RoundRobinReceptorTest.cpp',
    'src/ldk/tests/RoundRobinConnectorTest.cpp',
    'src/ldk/tests/RoundRobinDelivererTest.cpp',
    'src/ldk/tests/FlowSeparatorTest.cpp',
    'src/ldk/tests/FlowGateTest.cpp',
    'src/ldk/tests/GroupTest.cpp',
    'src/ldk/tests/GroupFlowSeparatorTest.cpp',
    'src/ldk/tests/SpeedTest.cpp',
    'src/ldk/tests/SizeCalculationTest.cpp',
    'src/ldk/tests/DropperTest.cpp',
    'src/ldk/tests/ClassifierTest.cpp',
    'src/ldk/tests/FUTestBase.cpp',
    'src/ldk/tests/FUTestBaseTest.cpp',
    'src/ldk/tests/DelayedInterfaceTest.cpp',
    'src/ldk/tests/CommandProxyTest.cpp',
    'src/ldk/fun/tests/FUNTest.cpp',
    'src/ldk/fun/tests/MainTest.cpp',
    'src/ldk/fun/tests/MainGenericTest.cpp',
    'src/ldk/fun/tests/SubTest.cpp',
    'src/ldk/fsm/tests/FunctionalUnitTest.cpp',
    'src/ldk/arq/tests/NoneTest.cpp',
    'src/ldk/arq/tests/StopAndWaitTest.cpp',
    'src/ldk/arq/tests/CumulativeACKTest.cpp',
    'src/ldk/arq/tests/SelectiveRepeatTest.cpp',
    'src/ldk/arq/tests/GoBackNTest.cpp',
    'src/ldk/arq/tests/PiggyBackerTest.cpp',
    'src/ldk/crc/tests/CRCTest.cpp',
    'src/ldk/crc/tests/CRCFilterTest.cpp',
    'src/ldk/buffer/tests/BoundedTest.cpp',
    'src/ldk/buffer/tests/DroppingTest.cpp',
    'src/ldk/sar/tests/FixedTest.cpp',
    'src/ldk/tools/tests/ForwarderTest.cpp',
    'src/ldk/tools/tests/ProducerTest.cpp',
    'src/ldk/tools/tests/ConsumerTest.cpp',
    'src/ldk/tools/tests/BridgeTest.cpp',
    'src/ldk/tools/tests/SynchronizerTest.cpp',
    'src/ldk/tools/tests/PaddingTest.cpp',
    'src/ldk/tools/tests/GateTest.cpp',
    'src/ldk/tools/tests/OverheadTest.cpp',
    'src/ldk/multiplexer/tests/OpcodeDelivererTest.cpp',
    'src/ldk/multiplexer/tests/OpcodeTest.cpp',
    'src/ldk/multiplexer/tests/DispatcherTest.cpp',
    'src/ldk/multiplexer/tests/FrameDispatcherTest.cpp',
    'src/ldk/fcf/tests/NewFrameProviderObserverTest.cpp',
    'src/ldk/probe/tests/PacketTest.cpp',
    'src/ldk/probe/tests/WindowTest.cpp',
    
    'src/fsm/tests/FSMTest.cpp',
]

hppFiles = [
'src/Average.hpp',
'src/Birthmark.hpp',
'src/Broker.hpp',
'src/Cache.hpp',
'src/CandI.hpp',
'src/Cloneable.hpp',
'src/CppUnit.hpp',
'src/DerefLess.hpp',
'src/Direction.hpp',
'src/Enumerator.hpp',
'src/Enum.hpp',
'src/Interval.hpp',
'src/Object.hpp',
'src/Ttos.hpp',
'src/Types.hpp',
'src/isClass.hpp',
'src/container/BinaryTree.hpp',
'src/container/Pool.hpp',
'src/container/RangeMap.hpp',
'src/container/Tree.hpp',
'src/container/Mapping.hpp',
'src/container/Matrix.hpp',
'src/container/MultiAccessible.hpp',
'src/container/tests/MatrixTest.hpp',
'src/distribution/Binomial.hpp',
'src/distribution/CDFTable.hpp',
'src/distribution/DiscreteUniform.hpp',
'src/distribution/Distribution.hpp',
'src/distribution/Erlang.hpp',
'src/distribution/Fixed.hpp',
'src/distribution/ForwardRecurrenceTime.hpp',
'src/distribution/Geometric.hpp',
'src/distribution/NegExp.hpp',
'src/distribution/Norm.hpp',
'src/distribution/Operation.hpp',
'src/distribution/Pareto.hpp',
'src/distribution/Poisson.hpp',
'src/distribution/RNGConfigCreator.hpp',
'src/distribution/Rice.hpp',
'src/distribution/TimeDependent.hpp',
'src/distribution/Uniform.hpp',
'src/distribution/tests/CDFTableTest.hpp',
'src/distribution/tests/DiscreteUniformTest.hpp',
'src/distribution/tests/ErlangTest.hpp',
'src/distribution/tests/FixedTest.hpp',
'src/distribution/tests/GeometricTest.hpp',
'src/distribution/tests/NegExpTest.hpp',
'src/distribution/tests/NormTest.hpp',
'src/distribution/tests/OperationTest.hpp',
'src/distribution/tests/ParetoTest.hpp',
'src/distribution/tests/PoissonTest.hpp',
'src/distribution/tests/RiceTest.hpp',
'src/distribution/tests/UniformTest.hpp',
'src/distribution/tests/VarEstimator.hpp',
'src/fsm/FSMConfigCreator.hpp',
'src/fsm/FSM.hpp',
'src/DoubleDispatcher.hpp',
'src/queuingsystem/Job.hpp',
'src/queuingsystem/JobContextProvider.hpp',
'src/queuingsystem/MM1Step1.hpp',
'src/queuingsystem/MM1Step6.hpp',
'src/queuingsystem/MM1Step3.hpp',
'src/queuingsystem/MM1Step5.hpp',
'src/queuingsystem/MM1Step2.hpp',
'src/queuingsystem/GGn.hpp',
'src/queuingsystem/Server.hpp',
'src/Assure.hpp',
'src/LongCreator.hpp',
'src/rng/RNGen.hpp',
'src/Singleton.hpp',
'src/RefCountable.hpp',
'src/Chamaeleon.hpp',
'src/Interpolation.hpp',
'src/ldk/arq/ARQ.hpp',
'src/ldk/arq/CumulativeACK.hpp',
'src/ldk/arq/GoBackN.hpp',
'src/ldk/arq/None.hpp',
'src/ldk/arq/PiggyBacker.hpp',
'src/ldk/arq/SelectiveRepeat.hpp',
'src/ldk/arq/statuscollector/Counter.hpp',
'src/ldk/arq/statuscollector/Interface.hpp',
'src/ldk/arq/statuscollector/None.hpp',
'src/ldk/arq/statuscollector/TwoSizesWindowed.hpp',
'src/ldk/arq/StopAndWait.hpp',
'src/ldk/arq/tests/PiggyBackerTest.hpp',
'src/ldk/buffer/Bounded.hpp',
'src/ldk/buffer/Buffer.hpp',
'src/ldk/buffer/Dropping.hpp',
'src/ldk/buffer/tests/BoundedTest.hpp',
'src/ldk/Classifier.hpp',
'src/ldk/command/FlowControl.hpp',
'src/ldk/Command.hpp',
'src/ldk/CommandPool.hpp',
'src/ldk/CommandProxy.hpp',
'src/ldk/CommandReaderInterface.hpp',
'src/ldk/CommandTypeSpecifier.hpp',
'src/ldk/CommandTypeSpecifierInterface.hpp',
'src/ldk/CompoundHandlerInterface.hpp',
'src/ldk/Compound.hpp',
'src/ldk/concatenation/Concatenation.hpp',
'src/ldk/Connector.hpp',
'src/ldk/ControlServiceInterface.hpp',
'src/ldk/crc/CRCFilter.hpp',
'src/ldk/crc/CRC.hpp',
'src/ldk/crc/tests/CRCTest.hpp',
'src/ldk/DelayedDeliveryInterface.hpp',
'src/ldk/Delayed.hpp',
'src/ldk/Deliverer.hpp',
'src/ldk/Dropper.hpp',
'src/ldk/ErrorRateProviderInterface.hpp',
'src/ldk/fcf/CompoundCollector.hpp',
'src/ldk/fcf/FrameBuilderConfigCreator.hpp',
'src/ldk/fcf/FrameBuilder.hpp',
'src/ldk/fcf/FrameBuilderPutter.hpp',
'src/ldk/fcf/NewFrameProviderObserver.hpp',
'src/ldk/fcf/PhaseDescriptor.hpp',
'src/ldk/fcf/TimingControl.hpp',
'src/ldk/FirstServeConnector.hpp',
'src/ldk/FlowGate.hpp',
'src/ldk/flowseparator/CreatorStrategy.hpp',
'src/ldk/flowseparator/FlowInfoProvider.hpp',
'src/ldk/FlowSeparator.hpp',
'src/ldk/flowseparator/NotFoundStrategy.hpp',
'src/ldk/Forwarding.hpp',
'src/ldk/fsm/CompoundHandlerSignalInterface.hpp',
'src/ldk/fsm/FunctionalUnit.hpp',
'src/ldk/FUNConfigCreator.hpp',
'src/ldk/FunctionalUnit.hpp',
'src/ldk/fun/FUN.hpp',
'src/ldk/fun/Main.hpp',
'src/ldk/fun/Sub.hpp',
'src/ldk/fun/tests/FUNTest.hpp',
'src/ldk/fun/tests/MainGenericTest.hpp',
'src/ldk/fun/tests/MainTest.hpp',
'src/ldk/fun/tests/SubTest.hpp',
'src/ldk/fu/Plain.hpp',
'src/ldk/Group.hpp',
'src/ldk/HasConnector.hpp',
'src/ldk/HasConnectorInterface.hpp',
'src/ldk/HasDeliverer.hpp',
'src/ldk/HasDelivererInterface.hpp',
'src/ldk/HasReceptor.hpp',
'src/ldk/HasReceptorInterface.hpp',
'src/ldk/helper/FakePDU.hpp',
'src/ldk/Key.hpp',
'src/ldk/LayerConfigCreator.hpp',
'src/ldk/Layer.hpp',
'src/ldk/ldk.hpp',
'src/ldk/LinkHandlerInterface.hpp',
'src/ldk/Link.hpp',
'src/ldk/ManagementServiceInterface.hpp',
'src/ldk/MultiLink.hpp',
'src/ldk/multiplexer/Dispatcher.hpp',
'src/ldk/multiplexer/FrameDispatcher.hpp',
'src/ldk/multiplexer/OpcodeDeliverer.hpp',
'src/ldk/multiplexer/OpcodeKey.hpp',
'src/ldk/multiplexer/OpcodeProvider.hpp',
'src/ldk/multiplexer/OpcodeSetter.hpp',
'src/ldk/multiplexer/tests/DispatcherTest.hpp',
'src/ldk/multiplexer/tests/FrameDispatcherTest.hpp',
'src/ldk/multiplexer/tests/OpcodeTest.hpp',
'src/ldk/probe/bus/Packet.hpp',
'src/ldk/probe/bus/Window.hpp',
'src/ldk/probe/ErrorRate.hpp',
'src/ldk/probe/Packet.hpp',
'src/ldk/probe/Probe.hpp',
'src/ldk/probe/Window.hpp',
'src/ldk/Processor.hpp',
'src/ldk/PyConfigCreator.hpp',
'src/ldk/RandomAccessLink.hpp',
'src/ldk/Receptor.hpp',
'src/ldk/RoundRobinConnector.hpp',
'src/ldk/RoundRobinDeliverer.hpp',
'src/ldk/RoundRobinLink.hpp',
'src/ldk/RoundRobinReceptor.hpp',
'src/ldk/sar/Fixed.hpp',
'src/ldk/sar/SAR.hpp',
'src/ldk/sar/Soft.hpp',
'src/ldk/SequentlyCallingLinkHandler.hpp',
'src/ldk/SimpleLinkHandler.hpp',
'src/ldk/SingleConnector.hpp',
'src/ldk/SingleDeliverer.hpp',
'src/ldk/SingleLink.hpp',
'src/ldk/SingleReceptor.hpp',
'src/ldk/SuspendableInterface.hpp',
'src/ldk/SuspendedInterface.hpp',
'src/ldk/SuspendSupport.hpp',
'src/ldk/tests/ClassifierTest.hpp',
'src/ldk/tests/DelayedInterfaceTest.hpp',
'src/ldk/tests/DropperTest.hpp',
'src/ldk/tests/FirstServeConnectorTest.hpp',
'src/ldk/tests/FlowSeparatorTest.hpp',
'src/ldk/tests/FunctionalUnitTest.hpp',
'src/ldk/tests/FUTestBase.hpp',
'src/ldk/tests/GroupFlowSeparatorTest.hpp',
'src/ldk/tests/LayerStub.hpp',
'src/ldk/tests/LayerTest.hpp',
'src/ldk/tests/MultiLinkTest.hpp',
'src/ldk/tests/RoundRobinConnectorTest.hpp',
'src/ldk/tests/SizeCalculationTest.hpp',
'src/ldk/tests/SpeedTest.hpp',
'src/ldk/tools/BottleNeckDetective.hpp',
'src/ldk/tools/Bridge.hpp',
'src/ldk/tools/Consumer.hpp',
'src/ldk/tools/DownUnconnectable.hpp',
'src/ldk/tools/FakeFU.hpp',
'src/ldk/tools/Forwarder.hpp',
'src/ldk/tools/Gate.hpp',
'src/ldk/tools/Overhead.hpp',
'src/ldk/tools/Padding.hpp',
'src/ldk/tools/PERProviderStub.hpp',
'src/ldk/tools/Producer.hpp',
'src/ldk/tools/Stub.hpp',
'src/ldk/tools/Stutter.hpp',
'src/ldk/tools/Synchronizer.hpp',
'src/ldk/tools/ConstantDelay.hpp',
'src/ldk/tools/tests/BridgeTest.hpp',
'src/ldk/tools/tests/ConsumerTest.hpp',
'src/ldk/tools/tests/ForwarderTest.hpp',
'src/ldk/tools/tests/GateTest.hpp',
'src/ldk/tools/tests/PaddingTest.hpp',
'src/ldk/tools/tests/ProducerTest.hpp',
'src/ldk/tools/UpUnconnectable.hpp',
'src/ldk/utils.hpp',
'src/logger/CoutOutput.hpp',
'src/logger/FormatStrategy.hpp',
'src/logger/SQLiteFormat.hpp',
'src/logger/OutputStrategy.hpp',
'src/logger/Master.hpp',
'src/logger/tests/LoggerTest.hpp',
'src/logger/tests/MasterTest.hpp',
'src/logger/tests/LoggerTestHelper.hpp',
'src/logger/tests/MessageTest.hpp',
'src/logger/FileOutput.hpp',
'src/logger/ConsoleFormat.hpp',
'src/logger/CerrOutput.hpp',
'src/logger/XMLFormat.hpp',
'src/logger/Message.hpp',
'src/logger/DelimiterFormat.hpp',
'src/logger/Logger.hpp',
'src/NonCopyable.hpp',
'src/SubjectInterface.hpp',
'src/SmartPtr.hpp',
'src/evaluation/statistics/stateval.hpp',
'src/evaluation/statistics/moments.hpp',
'src/evaluation/statistics/pdf.hpp',
'src/events/CanTimeout.hpp',
'src/events/NoOp.hpp',
'src/events/MemberFunction.hpp',
'src/events/PeriodicRealTimeout.hpp',
'src/events/PeriodicTimeout.hpp',
'src/events/MultipleTimeout.hpp',
'src/events/scheduler/CommandQueue.hpp',
'src/events/scheduler/Map.hpp',
'src/events/scheduler/Callable.hpp',
'src/events/scheduler/ICommand.hpp',
'src/events/scheduler/tests/InterfaceTest.hpp',
'src/events/scheduler/tests/PerformanceTest.hpp',
'src/events/scheduler/RealTime.hpp',
'src/events/scheduler/NullCommand.hpp',
'src/events/scheduler/Monitor.hpp',
'src/events/scheduler/INotification.hpp',
'src/events/scheduler/IEvent.hpp',
'src/events/scheduler/Interface.hpp',
'src/events/tests/PeriodicTimeoutTest.hpp',
'src/geometry/AABoundingBox.hpp',
'src/geometry/AxisParallelRectangle.hpp',
'src/geometry/LineSegment.hpp',
'src/geometry/Point.hpp',
'src/geometry/Shape2D.hpp',
'src/geometry/Vector.hpp',
'src/SmartPtrBase.hpp',
'src/Python.hpp',
'src/Subject.hpp',
'src/Functor.hpp',
'src/IOutputStreamable.hpp',
'src/PyConfigViewCreator.hpp',
'src/markovchain/ARMA.hpp',
'src/markovchain/MarkovBase.hpp',
'src/markovchain/MarkovContinuousTime.hpp',
'src/markovchain/MarkovContinuousTimeTraffic.hpp',
'src/markovchain/MarkovDiscreteTime.hpp',
'src/markovchain/MarkovDiscreteTimeTraffic.hpp',
'src/markovchain/tests/MarkovBaseTest.hpp',
'src/markovchain/tests/MarkovContinuousTimeTest.hpp',
'src/markovchain/tests/MarkovContinuousTimeTrafficTest.hpp',
'src/markovchain/tests/MarkovDiscreteTimeTest.hpp',
'src/markovchain/tests/MarkovDiscreteTimeTrafficTest.hpp',
'src/markovchain/TrafficSpec.hpp',
'src/module/Module.hpp',
'src/module/tests/ModuleTest.hpp',
'src/module/tests/MultiTypeFactoryTest.hpp',
'src/module/CurrentVersion.hpp',
'src/module/DateTime.hpp',
'src/module/DependencyList.hpp',
'src/module/Version.hpp',
'src/module/VersionInformation.hpp',
'src/module/Release.hpp',
'src/module/MultiTypeFactory.hpp',
'src/module/Base.hpp',
'src/node/Interface.hpp',
'src/node/Node.hpp',
'src/node/NodeSimulationModel.hpp',
'src/node/Registry.hpp',
'src/node/component/Component.hpp',
'src/node/component/ConfigCreator.hpp',
'src/node/component/FQSN.hpp',
'src/node/component/Interface.hpp',
'src/node/component/tests/ComponentStub.hpp',
'src/node/component/tests/ComponentTest.hpp',
'src/node/component/tests/FQSNTest.hpp',
'src/node/component/tests/IP.hpp',
'src/node/component/tests/TCP.hpp',
'src/node/tests/NodeTest.hpp',
'src/node/tests/Stub.hpp',
'src/NearestNeighbour.hpp',
'src/NLinear.hpp',
'src/osi/PCI.hpp',
'src/osi/PDU.hpp',
'src/probe/bus/ContextCollector.hpp',
'src/probe/bus/ContextProvider.hpp',
'src/probe/bus/ContextProviderCollection.hpp',
'src/probe/bus/utils.hpp',
'src/probe/bus/CompoundContextProvider.hpp',
'src/service/Service.hpp',
'src/service/dll/Address.hpp',
'src/service/dll/DataTransmission.hpp',
'src/service/dll/Handler.hpp',
'src/service/dll/ProtocolNumber.hpp',
'src/service/nl/Address.hpp',
'src/service/nl/tests/Address.hpp',
'src/service/nl/Service.hpp',
'src/service/nl/DataHandler.hpp',
'src/service/tl/Connection.hpp',
'src/service/tl/ConnectionHandler.hpp',
'src/service/tl/DataHandler.hpp',
'src/service/tl/FlowID.hpp',
'src/service/tl/PortPool.hpp',
'src/service/tl/Service.hpp',
'src/service/tl/TCPHeader.hpp',
'src/service/tl/UDPHeader.hpp',
'src/service/phy/power/OFDMAMeasurement.hpp',
'src/service/phy/power/PowerMeasurement.hpp',
'src/service/phy/ofdma/CarrierSensing.hpp',
'src/service/phy/ofdma/DataTransmission.hpp',
'src/service/phy/ofdma/Handler.hpp',
'src/service/phy/ofdma/MeasurementHandler.hpp',
'src/service/phy/ofdma/Measurements.hpp',
'src/service/phy/ofdma/Notification.hpp',
'src/service/phy/ofdma/Pattern.hpp',
'src/service/phy/phymode/MI2PERInterface.hpp',
'src/service/phy/phymode/PhyModeInterface.hpp',
'src/service/phy/phymode/PhyModeMapperInterface.hpp',
'src/service/phy/phymode/SNR2MIInterface.hpp',
'src/StaticFactoryBroker.hpp',
'src/Backtrace.hpp',
'src/simulator/Bit.hpp',
'src/simulator/Main.hpp',
'src/simulator/InterruptHandler.hpp',
'src/simulator/CPUTimeExhaustedHandler.hpp',
'src/simulator/ISimulator.hpp',
'src/simulator/IApplication.hpp',
'src/simulator/UnitTests.hpp',
'src/simulator/ISimulationModel.hpp',
'src/simulator/Time.hpp',
'src/simulator/SignalHandlerCallback.hpp',
'src/simulator/OutputPreparation.hpp',
'src/simulator/ProbeWriter.hpp',
'src/simulator/StatusReport.hpp',
'src/simulator/AbortHandler.hpp',
'src/simulator/Application.hpp',
'src/simulator/SignalHandler.hpp',
'src/simulator/SegmentationViolationHandler.hpp',
'src/simulator/Simulator.hpp',
'src/scheduler/SchedulerTypes.hpp',
'src/SlidingWindow.hpp',
'src/Exception.hpp',
'src/probe/bus/ContextFilterProbeBus.hpp',
'src/probe/bus/PassThroughProbeBus.hpp',
'src/probe/bus/PythonProbeBus.hpp',
'src/probe/bus/TableProbeBus.hpp',
'src/probe/bus/TextProbeBus.hpp',
'src/probe/bus/TimeSeriesProbeBus.hpp',
'src/probe/bus/tests/ProbeBusStub.hpp',
'src/probe/bus/SettlingTimeGuardProbeBus.hpp',
'src/probe/bus/LoggingProbeBus.hpp',
'src/probe/bus/ProbeBus.hpp',
'src/probe/bus/ProbeBusRegistry.hpp',
'src/probe/bus/Context.hpp',
'src/probe/bus/TimeWindowProbeBus.hpp',
'src/probe/bus/StatEvalProbeBus.hpp',
'src/probe/bus/detail/IProbeBusNotification.hpp',
'src/probe/bus/detail/MeasurementFunctor.hpp',
'src/probe/bus/detail/ObserverPimpl.hpp',
'src/probe/bus/detail/OutputFormatter.hpp',
'src/probe/bus/detail/SubjectPimpl.hpp',
'src/probe/bus/detail/Sorter.hpp',
'src/probe/bus/detail/StatEvalTable.hpp',
'src/PythonicOutput.hpp',
'src/pyconfig/helper/tests/FunctionsTest.hpp',
'src/pyconfig/helper/Functions.hpp',
'src/pyconfig/Parser.hpp',
'src/pyconfig/Converter.hpp',
'src/pyconfig/tests/SequenceTest.hpp',
'src/pyconfig/tests/ViewTest.hpp',
'src/pyconfig/tests/ParserTest.hpp',
'src/pyconfig/View.hpp',
'src/pyconfig/Sequence.hpp',
'src/pyconfig/Object.hpp',
'src/testing/DetailedListener.hpp',
'src/testing/TestTool.hpp',
'src/ObserverInterface.hpp',
'src/TypeInfo.hpp',
'src/StaticFactory.hpp',
'src/container/DynamicMatrix.hpp',
'src/container/FastListEnabler.hpp',
'src/container/Registry.hpp',
'src/container/FastListNode.hpp',
'src/container/FastList.hpp',
'src/container/UntypedRegistry.hpp',
'src/Conversion.hpp',
'src/TestFixture.hpp',
'src/demangle.hpp',
'src/StopWatch.hpp',
'src/Observer.hpp',
'src/tests/AverageTest.hpp',
'src/tests/EnumeratorTest.hpp',
'src/tests/IntervalTest.hpp',
'src/tests/CacheTest.hpp',
'src/tests/CandITest.hpp',
'src/tests/ClassTest.hpp',
'src/tests/CloneableTest.hpp',
'src/tests/DerefLessTest.hpp',
'src/tests/DirectionTest.hpp',
'src/tests/DoubleDispatcherTest.hpp',
'src/tests/EnumTest.hpp',
'src/tests/NearestNeighbourTest.hpp',
'src/tests/NLinearTest.hpp',
'src/tests/PositionableTest.hpp',
'src/tests/PowerRatioTest.hpp',
'src/tests/RoundRobinTest.hpp',
'src/tests/TimeWeightedAverageTest.hpp',
'src/tests/WeightedAverageTest.hpp',
'src/Positionable.hpp',
'src/Position.hpp',
'src/PositionObserver.hpp',
'src/PowerRatio.hpp',
'src/TimeWeightedAverage.hpp',
'src/TypeTraits.hpp',
'src/WeightedAverage.hpp',
'src/ReferenceModifier.hpp',
'src/RoundRobin.hpp',
]

pyconfig = [
'openwns/ARQ.py',
'openwns/CRC.py',
'openwns/Command.py',
'openwns/Tools.py',
'openwns/Group.py',
'openwns/Multiplexer.py',
'openwns/FCF.py',
'openwns/SAR.py',
'openwns/FUN.py',
'openwns/Buffer.py',
'openwns/PhyMode.py',
'openwns/ldk.py',
'openwns/Concatenation.py',
'openwns/distribution.py',
'openwns/FlowSeparator.py',
'openwns/Probe.py',
'openwns/node.py',
'openwns/simulator.py',
'openwns/queuingsystem.py',
'openwns/eventscheduler.py',
'openwns/rng.py',
'openwns/tests/simulatorTest.py',
'openwns/tests/__init__.py',
'openwns/tests/nodeTest.py',
'openwns/module.py',
'openwns/logger.py',
'openwns/probebus.py',
'openwns/interface.py',
'openwns/interval.py',
'openwns/pyconfig.py',
'openwns/__init__.py',
'openwns/backend/pyconfig.py',
'openwns/backend/__init__.py',
'openwns/evaluation/__init__.py',
'openwns/evaluation/formatters.py',
'openwns/evaluation/generators.py',
'openwns/evaluation/statistics.py',
'openwns/evaluation/tree.py',
'openwns/evaluation/wrappers.py',
'openwns/evaluation/default.py',
'openwns/geometry/position.py',
'openwns/geometry/__init__.py',
'openwns/tests/AbstractMethodTest.py',
'openwns/tests/__init__.py',

'openwns/markov/mmpp_example.gdf',
'openwns/markov/markov_onoff1.gdf',
]
libraries = []
Return('libname srcFiles hppFiles pyconfig libraries')
