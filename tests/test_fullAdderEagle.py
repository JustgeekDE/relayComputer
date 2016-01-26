from pkg_resources import resource_string

from unittest import TestCase

import os, sys
sys.path.insert(0, os.getcwd())

from scoville.circuit import Circuit
from scoville.signal import SignalWithResistance
from scoville.eagleSchematic import EagleSchematic

class SimulationUnitTest(TestCase):

  def getCircuit(self):
    schematicSource = resource_string('simulations', 'fullAdder.sch')
    schematic = EagleSchematic(schematicSource)
    circuit = Circuit(schematic.getSpiceData())

    circuit.inspectVoltage('OVERFLOW')
    circuit.inspectVoltage('RESULT')
    return circuit

  def testLowLowLowShouldResultInLowLow(self):
    circuit = self.getCircuit()

    circuit.setSignal(SignalWithResistance("BIT1", 0.0, 10))
    circuit.setSignal(SignalWithResistance("BIT2", 0.0, 10))
    circuit.setSignal(SignalWithResistance("BIT3", 0.0, 10))

    circuit.run()
    self.assertLess(circuit.getVoltage('OVERFLOW'), 0.5)
    self.assertLess(circuit.getVoltage('RESULT'), 0.5)

  def testHighHighHighShouldResultInHighHigh(self):
    circuit = self.getCircuit()

    circuit.setSignal(SignalWithResistance("BIT1", 12.0, 10))
    circuit.setSignal(SignalWithResistance("BIT2", 12.0, 10))
    circuit.setSignal(SignalWithResistance("BIT3", 12.0, 10))

    circuit.run()
    self.assertGreater(circuit.getVoltage('OVERFLOW'), 10.0)
    self.assertGreater(circuit.getVoltage('RESULT'), 10.0)

