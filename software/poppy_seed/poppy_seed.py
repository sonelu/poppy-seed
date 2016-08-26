import os
import numpy
import ctypes

from functools import partial

from poppy.creatures import AbstractPoppyCreature

from .primitives.posture import StandPosition, SitPosition
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

		for m in robot.motors:
			m.goto_behavior = 'dummy'

		for m in robot.torso:
			m.compliant_behavior = 'safe'

