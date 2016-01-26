from pkg_resources import resource_string

from unittest import TestCase

import os, sys
sys.path.insert(0, os.getcwd())

from scoville.circuit import Circuit
from scoville.signal import SignalWithResistance
from scoville.eagleSchematic import EagleSchematic

class SimulationUnitTest(TestCase):

  def getCircuit(self):
    schematicSource = resource_string('simulations', '2bitAdder.sch')
    schematic = EagleSchematic(schematicSource)
    circuit = Circuit(schematic.getSpiceData())

    circuit.inspectVoltage('OVERFLOW')
    circuit.inspectVoltage('R0')
    circuit.inspectVoltage('R1')
    return circuit

  def testZeroPlusZeroIsZero(self):
    circuit = self.getCircuit()

    circuit.setSignal(SignalWithResistance("A0", 0.0, 10))
    circuit.setSignal(SignalWithResistance("A1", 0.0, 10))
    circuit.setSignal(SignalWithResistance("B0", 0.0, 10))
    circuit.setSignal(SignalWithResistance("B1", 0.0, 10))

    circuit.run()
    self.assertLess(circuit.getVoltage('R0'), 0.5)
    self.assertLess(circuit.getVoltage('R1'), 0.5)
    self.assertLess(circuit.getVoltage('OVERFLOW'), 0.5)

  def ignored_testTwoPlusThreeIsFive(self):
    circuit = self.getCircuit()

    circuit.setSignal(SignalWithResistance("A0", 0.0, 10))
    circuit.setSignal(SignalWithResistance("A1", 12.0, 10))
    circuit.setSignal(SignalWithResistance("B0", 12.0, 10))
    circuit.setSignal(SignalWithResistance("B1", 12.0, 10))

    circuit.run()
    self.assertGreater(circuit.getVoltage('R0'), 10.0)
    self.assertLess(circuit.getVoltage('R1'), 0.5)
    self.assertGreater(circuit.getVoltage('OVERFLOW'), 10.0)

