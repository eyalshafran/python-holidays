# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import sys
import unittest

from datetime import date

import holidays


class TestEthiopia(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.ET()

    def test_2019(self):
        self.assertIn(date(2019, 1, 7), self.holidays)
        self.assertIn(date(2019, 1, 19), self.holidays)
        self.assertIn(date(2019, 3, 2), self.holidays)
        self.assertIn(date(2019, 4, 28), self.holidays)
        self.assertIn(date(2019, 4, 26), self.holidays)
        self.assertIn(date(2019, 5, 1), self.holidays)
        self.assertIn(date(2019, 5, 5), self.holidays)
        self.assertIn(date(2019, 5, 28), self.holidays)
        self.assertIn(date(2019, 9, 12), self.holidays)
        self.assertIn(date(2019, 9, 28), self.holidays)
        self.assertIn(date(2019, 11, 10), self.holidays)

    def test_ethiopian_christmas(self):
        self.assertIn(date(2019, 1, 7), self.holidays)

    def test_ethiopian_newyear(self):
        self.assertIn(date(2019, 9, 12), self.holidays)
        
    def test_ethiopian_meskel(self):
        self.assertIn(date(2019, 9, 28), self.holidays)

    def test_ethiopian_ephiphany(self):
        self.assertIn(date(2019, 1, 19), self.holidays)

    def test_adwa_victory(self):
        self.assertIn(date(2019, 3, 2), self.holidays)

    def test_easter_good_friday(self):
        self.assertIn(date(2019, 4, 26), self.holidays)

    def test_easter(self):
        self.assertIn(date(2019, 4, 28), self.holidays)

    def test_labour_day(self):
        self.assertIn(date(2019, 5, 1), self.holidays)
    
    def test_patriots_day(self):
        self.assertIn(date(2019, 5, 5), self.holidays)

    def test_downfall_of_dergue(self):
        self.assertIn(date(2019, 5, 28), self.holidays)


    def test_hijri_based(self):
        if sys.version_info.major >= (3, 6):
            import importlib.util

            if importlib.util.find_spec("hijri_converter"):
                self.holidays = holidays.ET(years=[2010])
                self.assertIn(date(2019, 6, 4), self.holidays)
                self.assertIn(date(2019, 8, 11), self.holidays)
                self.assertIn(date(2019, 11, 10), self.holidays)
                # eid_alfitr
                self.assertIn(date(2019, 6, 4), self.holidays)
                # eid_aladha
                self.assertIn(date(2019, 8, 11), self.holidays)
                # muhammad's birthday
                self.assertIn(date(2019, 11, 10), self.holidays)
                # eid_elfetr_2010
                self.assertIn(date(2010, 9, 10), self.holidays)
                # arafat_2010
                self.assertIn(date(2010, 11, 15), self.holidays)
                # muhammad's birthday2010
                self.assertIn(date(2010, 2, 26), self.holidays)
