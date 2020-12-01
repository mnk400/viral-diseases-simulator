import random
import numpy as np
from numpy.core.fromnumeric import size
from src.population import Population
import src.person_properties_util as index
from src.virus_util import Virus
from src.movements import Movement

class PopulationUtil(object):
    """
    Class representing the self.person.persons 
    """

    #_instance = Population()
    # def getInstance():
    #     return Population._instance

    def __init__(self, size: int, r: float, k: float, min_age : int, max_age: int, mortality_rate: int,
                    social_distance_per: int, infection_range: float, recovery_time: int, total_healthcare_capacity: int,
                    mask_effectiveness: dict, speed: float):
        """
        Constructor used for initializing the bound for the x axis, y axis, the k and R value for the particular population

        Parameters
        ----------
        size : int
            Size of the population
        x_bounds : list
            The list containing the lower and upper bound for the x axis of the population map
        y_bounds : list
            The list containing the lower and upper bound for the y axis of the population map
        r : float
            Disease reproduction (R0) rate for the virus
        k : float
            The k value for the virus
        """        
        self.population                 = Population(size) 
        self.virus                      = Virus(infection_range, recovery_time, total_healthcare_capacity)
        self.movement                   = Movement()
        self.size                       = size
        self.x_bounds                   = [0, 1]
        self.y_bounds                   = [0, 1]
        self.k                          = k
        self.r                          = r
        self.destinations               = np.random.uniform(low=0,high=1,size=(self.size,2))
        self.min_age                    = min_age
        self.max_age                    = max_age
        self.mortality_rate             = mortality_rate
        self.social_distance_per        = social_distance_per
        self.mask_effectiveness         = mask_effectiveness
        self.speed                      = speed
        self.persons                    = self.population.get_person()
        

        self.initialize_persons()

    def initialize_persons(self):
        """
        Method which initializes the person list in the population and further calls another method to update other 
        properties of the individual persons
        """    
        self.population.initialize_id(0, self.size)
        self.population.initialize_ages(self.min_age, self.max_age, self.size)
        self.population.initialize_positions(self.x_bounds, self.y_bounds, self.size)
        self.population.initialize_g_value(self.r, 1/self.k, self.size)
        self.population.initialize_mask_eff(self.size, self.mask_effectiveness)
        self.population.initialize_mortality_rate(self.size, self.mortality_rate)
        self.population.initialize_social_distancing(self.social_distance_per)
        
        self.population.initialize_susceptibility()
        # print(self.persons[:,15])
        self.persons[:, 7] = 1
        self.persons[:,10] = 0.1
        self.persons[:,11] = 0.1

        #self.persons[:, index.social_distance] = tmp
        #Update the destination each person is headed to and corresponding speed randomly
        self.persons = self.movement.update_persons(self.persons, self.size, self.speed, 1)
        self.persons[62, index.g_value] = 3
        self.population.set_infected_at(62, 0)
        self.persons[62, index.social_distance] = 0
        self.persons[62, 9] = 1


    def move(self, frame):
        # print(self.persons)
        active_dests = len(self.persons[self.persons[:,7] != 0])
 
        #print(active_dests)
        # if active_dests > 0 and len(self.persons[self.persons[:,8] == 0]) > 0:
        #     #print("here1")
        #     self.persons = self.movement.set_destination(self.persons, self.destinations, self.population)
        #     self.persons = self.movement.check_at_destination(self.persons, self.destinations)

        # if active_dests > 0 and len(self.persons[self.persons[:,8] == 1]) > 0:
        #     self.persons = self.movement.keep_at_destination(self.persons, self.destinations)
        #     #pass
        
        _xbounds = np.array([[0,1]] * self.size)
        _ybounds = np.array([[0,1]] * self.size)
        self.persons = self.movement.out_of_bounds(self.persons, _xbounds, _ybounds)

        self.persons = self.movement.update_persons(self.persons, self.size, self.speed)
        
        self.persons = self.movement.update_pop(self.persons)

        self.population = self.virus.infect(self.population, frame)

if __name__ == "__main__":
    # p = Population(100, [0, 1], [0, 1], 3, 0.5)
    #p.move()
    #virus = Virus()
    #p.person = virus.infect(p.person)
    pass
    



            


