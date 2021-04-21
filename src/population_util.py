'''
Created on Nov 29, 2020
@author: Pallak Singh, manik
'''
import numpy as np
from src.population import Population
import src.person_properties_util as index
from src.virus_util import Virus
from src.movements import Movement


class PopulationUtil(object):
    """
    Class representing the self.person.persons
    """

    def __init__(self, size: int, r: float, k: float, min_age: int,
                 max_age: int, mortality_rate: int, social_distance_per: int,
                 infection_range: float, recovery_time: int,
                 total_healthcare_capacity: int, mask_effectiveness: dict,
                 speed: float, social_distancing_at: int,
                 mask_wearing_at: int):
        """
        Constructor used for initializing the bound for the x axis, y axis,
        the k and R value for the particular population.

        Parameters
        ----------
        size : int
            Size of the population
        x_bounds : list
            The list containing the lower and upper bound for the x axis of
            the population map
        y_bounds : list
            The list containing the lower and upper bound for the y axis of
            the population map
        r : float
            Disease reproduction (R0) rate for the virus
        k : float
            The k value for the virus
        """
        self.population = Population(size)
        self.virus = Virus(infection_range, recovery_time,
                           total_healthcare_capacity)
        self.recovery_time = recovery_time
        self.total_healthcare_capacity = total_healthcare_capacity
        self.movement = Movement()
        self.size = size
        self.x_bounds = [0, 1]
        self.y_bounds = [0, 1]
        self.k = k
        self.r = r
        self.destinations = np.random.uniform(low=0, high=1,
                                              size=(self.size, 2))
        self.min_age = min_age
        self.max_age = max_age
        self.mortality_rate = mortality_rate
        self.social_distance_per = social_distance_per
        self.mask_effectiveness = mask_effectiveness
        self.speed = speed
        self.persons = self.population.get_person()
        self.enforce_social_distance_at = social_distancing_at
        self.enforce_mask_wearing_at = mask_wearing_at
        self.social_distancing_enforced = False
        self.mask_wearing_enforced = False
        self.initialize_persons()

    def initialize_persons(self):
        """
        Method which initializes the person list in the population and further
        calls another method to update other properties of the individual
        persons.
        """
        self.population.initialize_id(0, self.size)
        self.population.initialize_ages(self.min_age, self.max_age, self.size)
        self.population.initialize_positions(self.x_bounds, self.y_bounds,
                                             self.size)
        self.population.initialize_g_value(self.r, 1/self.k, self.size)
        self.population.initialize_mortality_rate(self.size,
                                                  self.mortality_rate)
        self.population.initialize_susceptibility()
        self.population.initialize_infected_by()

        self.persons[:, 7] = 1
        self.persons[:, 10] = 0.1
        self.persons[:, 11] = 0.1

        # Update the destination each person is headed to and corresponding
        # speed randomly
        self.persons = self.movement.update_persons(self.persons, self.size,
                                                    self.speed, 1)

        self.infected_person = np.random.randint(0, self.size)
        self.persons[self.infected_person, index.g_value] = 3
        self.population.set_infected_at(self.infected_person, 0)
        self.persons[self.infected_person, index.infected_by] = \
            self.infected_person
        self.persons[self.infected_person, index.social_distance] = 0
        self.persons[self.infected_person, 9] = 1

    def move(self, frame):
        if frame == self.enforce_mask_wearing_at:
            self.population.initialize_mask_eff(self.size,
                                                self.mask_effectiveness)
            self.population.initialize_susceptibility()
            self.mask_wearing_enforced = True

        if frame == self.enforce_social_distance_at:
            self.population \
                .initialize_social_distancing(self.social_distance_per)
            self.persons[self.infected_person, index.social_distance] = 0
            self.social_distancing_enforced = True

        if frame >= self.enforce_social_distance_at and \
                frame % 300 == 0 and self.enforce_social_distance_at >= 0:
            self.population \
                .initialize_social_distancing(self.social_distance_per)

        _xbounds = np.array([[0, 1]] * self.size)
        _ybounds = np.array([[0, 1]] * self.size)

        self.persons = self.movement.out_of_bounds(self.persons, _xbounds,
                                                   _ybounds)
        self.persons = self.movement.update_persons(self.persons, self.size,
                                                    self.speed)

        self.persons = self.movement.update_pop(self.persons)
        self.population = self.virus.infect(self.population, frame)
