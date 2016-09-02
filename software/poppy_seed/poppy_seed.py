import os
import numpy
import ctypes

from functools import partial

from poppy.creatures import AbstractPoppyCreature

from .primitives.posture import StandPosition, SitPosition
from .primitives.safe import LimitTorque, TemperatureMonitor, VoltageMonitor
"""
we'll deal with these later

from .primitives.safe import LimitTorque, TemperatureMonitor
from .primitives.dance import SimpleBodyBeatMotion
from .primitives.idle import UpperBodyIdleMotion, HeadIdleMotion
from .primitives.interaction import ArmsTurnCompliant, PuppetMaster
"""

class PoppySeed(AbstractPoppyCreature):

	@classmethod
	def setup(cls, robot):
		robot._primitive_manager._filter = partial(numpy.sum, axis=0)

		"""
		for m in robot.motors:
			m.goto_behavior = 'dummy'

		for m in robot.torso:
			m.compliant_behavior = 'safe'
		"""

        # basic primitives:
		robot.attach_primitive(StandPosition(robot), 'stand_position')
		#robot.attach_primitive(SitPosition(robot), 'sit_position')

        # Safe primitives:
		robot.attach_primitive(LimitTorque(robot), 'limit_torque')
		robot.limit_torque.start()
		if not robot.simulated:
			sound_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      'media', 'sounds', 'high_temperature.wav')
			robot.attach_primitive(TemperatureMonitor(robot, sound=sound_file), 'temperature_monitoring')
			robot.temperature_monitoring.start()

		if not robot.simulated:
			sound_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      'media', 'sounds', 'low_voltage.wav')
			robot.attach_primitive(VoltageMonitor(robot, sound=sound_file), 'voltage_monitoring')
			robot.voltage_monitoring.start()
