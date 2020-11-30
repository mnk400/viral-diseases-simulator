from pandas.core.tools.numeric import to_numeric
from config_util import ConfigUtil
from population import Population
import numpy as np
import math
import random
from time import sleep
import person_properties_util as index

class Virus():
    """
    This class provides abstraction to all virus related properties and methods such as 
    infecting, healing and dying
    """    

    def __init__(self):
        """
        The constructor is responsible for loading the virus statistics from the config file
        """  
        config = ConfigUtil("config/config.ini")
        self.infection_range        = config.getFloatValue("virus.stats", "infection_range")
        self.k_value                = config.getFloatValue("virus.stats", "k_value")
        self.reproduction_rate      = config.getFloatValue("virus.stats", "reproduction_rate")
        self.mortality_rate         = config.getFloatValue("virus.stats", "mortality_rate")
        self.mask_effectiveness     = config.getFloatValue("virus.stats", "mask_effectiveness")
        self.recovery_time          = config.getFloatValue("virus.stats", "recovery_time")
        
    def infect(self, population: Population):

        #Get the index of all the people who were infected in the previous step
        infected_idx = population.get_all_infected()
        
        persons = population.get_person()
        
        infected_to_be = []
        #print(len(population.persons[:,index.g_value == 0]))
        #print(population.persons[62][index.g_value])

        for idx in infected_idx:
            x_bounds = [persons[int(idx[0])][index.x_axis] - math.sqrt(self.infection_range), persons[int(idx[0])][index.x_axis] + math.sqrt(self.infection_range)]
            y_bounds = [persons[int(idx[0])][index.y_axis] - math.sqrt(self.infection_range), persons[int(idx[0])][index.y_axis] + math.sqrt(self.infection_range)]
            #print(x_bounds)
            #print(y_bounds)
            
            tmp = self.find_nearby(persons, x_bounds, y_bounds)
            #print(tmp)

            for i in tmp:
                chance = np.random.uniform(low = 0, high = 1)
                if chance<persons[int(idx[0])][13] and persons[int(idx[0])][index.g_value] > 0:
                    population.persons[int(i)][9] = 1
                    population.persons[int(idx[0])][index.g_value] -= 1
        return population

    
    def find_nearby(self, persons: np.ndarray, x_bounds: list, y_bounds: list) -> list:
        """
        Find the nearby per

        Parameters
        ----------
        person : Person
            [description]
        x_bounds : list
            [description]
        y_bounds : list
            [description]

        Returns
        -------
        list
            [description]
        """        
        
        selected_rows = persons[:,0][(x_bounds[0]<persons[:, index.x_axis]) &
                                        (x_bounds[1]>persons[:, index.x_axis]) &
                                        (y_bounds[0]<persons[:, index.y_axis]) &
                                        (y_bounds[1]>persons[:, index.y_axis]) &
                                        (persons[:, index.current_state] == 0)
                                    ]
      
        return selected_rows
    