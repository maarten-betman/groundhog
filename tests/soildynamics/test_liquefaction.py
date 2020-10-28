#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Bruno Stuyts'

# Native Python packages
import unittest
import os

# 3rd party packages
import pandas as pd
import numpy as np

# Project imports
from groundhog.soildynamics import liquefaction


class Test_liquefaction(unittest.TestCase):

    def test_cyclicstressratio_moss(self):
        result = liquefaction.cyclicstressratio_moss(
            sigma_vo=86.3,
            sigma_vo_eff=59.32,
            magnitude=5.9,
            acceleration=0.19 * 9.81,
            depth=5
        )
        self.assertAlmostEqual(
            result['rd [-]'], 0.92, 2
        )
        self.assertAlmostEqual(
            result['DWF [-]'], 1.410, 3
        )
        self.assertAlmostEqual(
            result['CSR [-]'], 0.166, 3
        )
        self.assertAlmostEqual(
            result['CSR* [-]'], 0.117, 3
        )

    def test_liquefactionprobability_moss(self):
        result = liquefaction.liquefactionprobability_moss(
            qc=10,
            sigma_vo_eff=80,
            Rf=1.5,
            CSR=0.4,
            CSR_star=0.32
        )
        self.assertAlmostEqual(
            result['qc_5 [MPa]'], 14.31, 2
        )
        self.assertAlmostEqual(
            result['qc_95 [MPa]'], 9.74, 2
        )
        self.assertAlmostEqual(
            result['Pl [pct]'], 43, 0
        )
