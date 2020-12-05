
import unittest
from src.population import Population
from config_util import ConfigUtil
from virus_util import Virus
from src.population_util import PopulationUtil
import logging
import functools
import numpy as np
import src.person_properties_util as index


class VirusUtilTest(unittest.TestCase):

    def setUp(self) -> None:

        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info('Testing virus util class.....')
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
        self.virus_util = Virus(self.infection_range, self.recovery_time, self.total_healthcare_capacity)

    def test_infect(self):

        before_infect_population = self.population_util.population.get_all_infected()

        self.infected_person = np.random.randint(0, self.size)
        self.population_util.population.persons[self.infected_person, index.g_value] = 3
        self.population_util.population.set_infected_at(1, 0)
        self.population_util.population.persons[self.infected_person, index.social_distance] = 0
        self.population_util.population.persons[self.infected_person, 9] = 1
        infected_population = self.virus_util.infect(self.population_util.population, 2)
        self.assertIsInstance(infected_population, Population)

        if functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, before_infect_population[:, 9], infected_population.get_all_infected()[:, 9]), True):
            self.assertTrue(False, "Test failed, infect did not work")
        else:
            self.assertTrue(True, "Test passed, infect method worked")

    def test_die_or_immune(self):

        dead_frame_1 = self.population_util.population.get_all_dead()
        self.assertEqual(len(dead_frame_1), 0)