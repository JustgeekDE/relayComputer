from pkg_resources import resource_string

from unittest import TestCase

import os, sys
sys.path.insert(0, os.getcwd())

from scoville.circuit import Circuit
from scoville.signal import SignalWithResistance, DelayedSignal

class SimulationUnitTest(TestCase):

  def getCircuit(self):
    relaySource = resource_string('simulations', 'halfAdder.cir')
    circuit = Circuit(relaySource)

    circuit.inspectVoltage('overflow')
    circuit.inspectVoltage('result')
    return circuit

  def testLowLowShouldResultInLowLow(self):
    circuit = self.getCircuit()

    circuit.setSignal(SignalWithResistance("bit1", 0.0, 10))
    circuit.setSignal(SignalWithResistance("bit2", 0.0, 10))

    circuit.run()
    self.assertLess(circuit.getVoltage('overflow'), 0.5)
    self.assertLess(circuit.getVoltage('result'), 0.5)

  def testLowHighShouldResultInLowHigh(self):
    circuit = self.getCircuit()

    circuit.setSignal(SignalWithResistance("bit1", 0.0, 10))
    circuit.setSignal(SignalWithResistance("bit2", 12.0, 10))

    circuit.run()
    self.assertLess(circuit.getVoltage('overflow'), 0.5)
    self.assertGreater(circuit.getVoltage('result'), 6.0)

  def testHighLowShouldResultInLowHigh(self):
    circuit = self.getCircuit()

    circuit.setSignal(SignalWithResistance("bit1", 12.0, 10))
    circuit.setSignal(SignalWithResistance("bit2", 0.0, 10))

    circuit.run()
    self.assertLess(circuit.getVoltage('overflow'), 0.5)
    self.assertGreater(circuit.getVoltage('result'), 6.0)

  def testHighHighShouldResultInHighLow(self):
    circuit = self.getCircuit()

    circuit.setSignal(SignalWithResistance("bit1", 12.0, 10))
    circuit.setSignal(SignalWithResistance("bit2", 12.0, 10))

    circuit.run()
    self.assertGreater(circuit.getVoltage('overflow'), 6.0)
    self.assertLess(circuit.getVoltage('result'), 0.5)
