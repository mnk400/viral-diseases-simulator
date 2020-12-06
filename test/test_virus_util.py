"""
Test file for population util class

Created on Dec 5th, 2020
@author: Yatish Pitta
"""
import unittest
from src.population import Population
from src.config_util import ConfigUtil
from src.virus_util import Virus
import logging
import numpy as np
import src.person_properties_util as index
from src.movements import Movement


class VirusUtilTest(unittest.TestCase):
    """
    Test case to test the Virus class
    """

    def setUp(self) -> None:
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info('Testing virus util class.....')
        self.config_util = ConfigUtil('config/test_config.ini')
        self.k = self.config_util.getFloatValue("virus.stats", "k_value")
        self.r = self.config_util.getFloatValue("virus.stats", "r_value")
        self.size = 10
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
        self.x_bounds = [0, 1]
        self.y_bounds = [0, 1]
        self.population = Population(self.size)
        self.population.initialize_id(0, self.size)
        self.population.initialize_ages(self.min_age, self.max_age, self.size)
        self.population.initialize_positions(self.x_bounds, self.y_bounds, self.size)
        self.population.initialize_g_value(self.r, 1 / self.k, self.size)
        self.population.initialize_mortality_rate(self.size, self.mortality_rate)
        self.population.initialize_susceptibility()
        self.virus_util = Virus(1, self.recovery_time, self.total_healthcare_capacity)
        self.population.persons[:, 7] = 1
        self.population.persons[:, 10] = 0.1
        self.population.persons[:, 11] = 0.1
        self.movement = Movement()

    def test_infect(self):
        """
        Test case to test the infect method;
        Compares the number of infected people before and after calling the infect method
        """
        before_infect_population = self.population.get_all_infected()
        self.population.persons = self.movement.update_persons(self.population.persons, self.size, self.speed, 1)
        self.infected_person = np.random.randint(0, self.size)
        self.population.persons[self.infected_person, index.g_value] = 3
        self.population.set_infected_at(1, 0)
        self.population.persons[self.infected_person, index.social_distance] = 0
        self.population.persons[self.infected_person, 9] = 1
        _xbounds = np.array([[0, 1]] * self.size)
        _ybounds = np.array([[0, 1]] * self.size)

        for i in range(1, self.size):
            self.population.persons = self.movement.out_of_bounds(self.population.persons, _xbounds, _ybounds)

            self.population.persons = self.movement.update_persons(self.population.persons, self.size, self.speed, 1)

            self.population.persons = self.movement.update_pop(self.population.persons)

            self.population = self.virus_util.infect(self.population, i)

        self.assertTrue(len(before_infect_population[:, 9]) != len(self.population.get_all_infected()[:, 9]) and len(
            self.population.get_all_infected()[:, 9]) > 1, "Test failed, infect did not work")

    def test_die_or_immune(self):
        """
        Test case to test the die_or_immune method
        """
        dead_frame_1 = self.population.get_all_dead()
        self.assertEqual(len(dead_frame_1), 0)

        self.population.persons = self.movement.update_persons(self.population.persons, self.size, self.speed, 1)
        self.infected_person = np.random.randint(0, self.size)
        self.population.persons[self.infected_person, index.g_value] = 3
        self.population.set_infected_at(1, 0)
        self.population.persons[self.infected_person, index.social_distance] = 0
        self.population.persons[self.infected_person, 9] = 1
        _xbounds = np.array([[0, 1]] * self.size)
        _ybounds = np.array([[0, 1]] * self.size)

        for i in range(1, self.size):
            self.population.persons = self.movement.out_of_bounds(self.population.persons, _xbounds, _ybounds)

            self.population.persons = self.movement.update_persons(self.population.persons, self.size, self.speed, 1)

            self.population.persons = self.movement.update_pop(self.population.persons)

            self.population = self.virus_util.infect(self.population, i)
        self.population.persons[:, index.mortality_rate] = 1.00
        self.virus_util.die_or_immune(self.population, int(self.population.get_all_infected()[0][0]))
        self.assertNotEqual(len(self.population.get_all_dead()), 0)
