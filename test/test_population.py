"""
Test file for population class

Created on Dec 2nd, 2020
@author: Yatish Pitta
"""
import logging
import unittest
from config_util import ConfigUtil
from population_util import Population
import numpy as np


class PopulationClassTest(unittest.TestCase):
    """
    Test cases to test the granular functionality of Population class
    """

    def setUp(self) -> None:
        """
        Setup method initializes all necessary variables from the configuration file and also creates an instance of the Population class
        """
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info('Testing population class.....')
        self.config_util = ConfigUtil('config/test_config.ini')
        self.k = self.config_util.getFloatValue("virus.stats", "k_value")
        self.r = self.config_util.getFloatValue("virus.stats", "r_value")
        self.size = self.config_util.getIntegerValue("area.stats", "total_population")
        self.min_age = self.config_util.getIntegerValue("people.stats", "min_age")
        self.max_age = self.config_util.getIntegerValue("people.stats", "min_age")
        self.mortality_rate = self.config_util.getDictionary("virus.stats", "mortality_rate")
        self.social_distance_per = self.config_util.getFloatValue("people.stats", "social_distancing_percent")
        self.infection_range = self.config_util.getFloatValue("virus.stats", "infection_range")
        self.recovery_time = self.config_util.getFloatValue("virus.stats", "recovery_time")
        self.total_healthcare_capacity = self.size * (
                    self.config_util.getIntegerValue("area.stats", "healthcare_capacity_ratio") / 100)
        self.mask_effectiveness = self.config_util.getDictionary("virus.stats", "mask_effectiveness")
        self.speed = self.config_util.getFloatValue("people.stats", "speed")
        self.enforce_social_distance_at = self.config_util.getIntegerValue("area.stats", "enforce_social_distancing_at")
        self.enforce_mask_wearing_at = self.config_util.getIntegerValue("area.stats", "enforce_mask_wearing_at")
        self.x_bounds = [0, 1]
        self.y_bounds = [0, 1]
        self.population = Population(self.size)

    def initialize(self):
        """
        Method Calls all the initialize functions from the Population class
        """
        self.population.initialize_id(0, self.size)
        self.population.initialize_ages(self.min_age, self.max_age, self.size)
        self.population.initialize_positions(self.x_bounds, self.y_bounds, self.size)
        self.population.initialize_g_value(self.r, 1 / self.k, self.size)
        self.population.initialize_mortality_rate(self.size, self.mortality_rate)
        self.population.initialize_mask_eff(self.size, self.mask_effectiveness)
        self.population.initialize_social_distancing(self.social_distance_per)
        self.population.initialize_susceptibility()

    def tearDown(self) -> None:
        pass

    def test_get_people(self):
        """
        Test to check if the population has been created of a correct size
        """
        assert isinstance(self.population.get_person(), np.ndarray)
        self.assertEqual(self.size, self.population.get_person()[:, 0].size)

    def test_get_people_by_health(self):
        """
        Test to check if the people at indices returned by get_all_healthy are actually healthy;
        people returned by get_all_infected are actually infected;
        people returned by get_all_recovered are actually recovered;
        people returned by get_all_dead are dead;
        """
        persons = self.population.get_person()

        # Test if get_all_infected returns indices of all people infected
        self.assertEqual(persons[persons[:, 9] == 1].size, self.population.get_all_infected().size)

        # Test if get_all_healthy returns indices of all people healthy
        self.assertEqual(persons[persons[:, 9] == 0].size, self.population.get_all_healthy().size)

        # Test if get_all_recovered returns indices of all people who recovered
        self.assertEqual(persons[persons[:, 9] == 2].size, self.population.get_all_recovered().size)

        # Test if get_all_dead returns indices of all people dead
        self.assertEqual(persons[persons[:, 9] == 3].size, self.population.get_all_dead().size)

    def test_get_currently_active(self):
        """
        Test to check if get_currently_active returns correct information
        """
        for i in self.population.get_currently_active_info():
            if int(i) != 0 and int(i) != 1:
                self.assertTrue(False, "Array contains values other than 0 and 1")
        self.assertTrue(True, "Array contains either 0 or 1")


if __name__ == '__main__':
    unittest.main()
