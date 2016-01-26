from pkg_resources import resource_string

from unittest import TestCase

import os, sys
sys.path.insert(0, os.getcwd())

from scoville.circuit import Circuit
from scoville.signal import SignalWithResistance, DelayedSignal

class SimulationUnitTest(TestCase):

  def getCircuit(self):
    relaySource = resource_string('simulations', 'relayExample.cir')
    circuit = Circuit(relaySource)

    circuit.inspectVoltage('OUT')
    return circuit

  def testLowShouldResultInLow(self):
    circuit = self.getCircuit()

    circuit.setSignal(SignalWithResistance("IN", 0.0, 10))

    circuit.run()
    self.assertLess(circuit.getVoltage('OUT'), 0.5)

  def testHighShouldResultInHigh(self):
    circuit = self.getCircuit()

    circuit.setSignal(SignalWithResistance("IN", 12.0, 10))

    circuit.run()
    self.assertGreater(circuit.getVoltage('OUT'), 6.0)

