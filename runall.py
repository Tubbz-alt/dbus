#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys

from dde_control_center.system_info import SystemInfo
from dde_daemon import DaemonDock, Keybinding, Display

testClasses = (SystemInfo, DaemonDock, Keybinding, Display)

suitelist = []

for c in testClasses:
    suitelist.append(c.suite())

alltests = unittest.TestSuite(tuple(suitelist))

runner = unittest.TextTestRunner()
runner.run(alltests)
