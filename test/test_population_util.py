"""
Test file for population util class

Created on Dec 4th, 2020
@author: Yatish Pitta
"""
import logging
import unittest
from config_util import ConfigUtil
from population_util import PopulationUtil
import functools


class PopulationUtilClassTest(unittest.TestCase):
    """
    Test cases to test the granular functionality of Population util class
    """

    def setUp(self) -> None:
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info('Testing population util class.....')
        self.config_util = ConfigUtil('config/test_config.ini')
        self.k                          = self.config_util.getFloatValue("virus.stats", "k_value")
        self.r                          = self.config_util.getFloatValue("virus.stats", "r_value")
        self.size                       = self.config_util.getIntegerValue("area.stats", "total_population")
        self.min_age                    = self.config_util.getIntegerValue("people.stats", "min_age")
        self.max_age                    = self.config_util.getIntegerValue("people.stats", "min_age")
        self.mortality_rate             = self.config_util.getDictionary("virus.stats", "mortality_rate")
        self.social_distance_per        = self.config_util.getFloatValue("people.stats", "social_distancing_percent")
        self.infection_range            = self.config_util.getFloatValue("virus.stats", "infection_range")
        self.recovery_time              = self.config_util.getFloatValue("virus.stats", "recovery_time")
        self.total_healthcare_capacity  = self.size*(self.config_util.getIntegerValue("area.stats", "healthcare_capacity_ratio")/100)
        self.mask_effectiveness         = self.config_util.getDictionary("virus.stats", "mask_effectiveness")
        self.speed                      = self.config_util.getFloatValue("people.stats", "speed")
        self.enforce_social_distance_at = self.config_util.getIntegerValue("area.stats", "enforce_social_distancing_at")
        self.enforce_mask_wearing_at    = self.config_util.getIntegerValue("area.stats", "enforce_mask_wearing_at")
        self.initialize()

    def initialize(self) -> None:
        """
        Initializes the population util class with the appropriate parameters
        """
        self.population_util = PopulationUtil(k=self.k, r=self.r, min_age=self.min_age, max_age=self.max_age,
                                                  size=self.size,
                                                  mortality_rate=self.mortality_rate,
                                                  infection_range=self.infection_range,
                                                  recovery_time=self.recovery_time,
                                                  total_healthcare_capacity=self.total_healthcare_capacity,
                                                  social_distance_per=self.social_distance_per,
                                                  mask_effectiveness=self.mask_effectiveness, speed=self.speed,
                                                  social_distancing_at=self.enforce_social_distance_at,
                                                  mask_wearing_at=self.enforce_mask_wearing_at)

    def test_move(self):
        """
        Tests the move method to check if the position of the persons is changing
        """

        try:
            x_axis_before = list(self.population_util.population.get_x_axis())
            y_axis_before = list(self.population_util.population.get_y_axis())
            self.population_util.move(1)
            x_axis_after = list(self.population_util.population.get_x_axis())
            y_axis_after = list(self.population_util.population.get_y_axis())
            if functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, x_axis_before, x_axis_after), True):
                self.assertTrue(False, "Test failed, x axis values did not change")
            else:
                self.assertTrue(True, "Test passed, x axis values changed")

            if functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, y_axis_before, y_axis_after), True):
                self.assertTrue(False, "Test failed, y axis values did not change")
            else:
                self.assertTrue(True, "Test passed, y axis values changed")
        except Exception as e:
            self.assertTrue(False, 'Test failed')
            logging.error('Error occured '+e)