from pandas.core.tools.numeric import to_numeric
from src.config_util import ConfigUtil
from src.population import Population
import numpy as np
import math
from time import sleep
import src.person_properties_util as index

class Virus():
    """
    This class provides abstraction to all virus related properties and methods such as 
    infecting, healing and dying
    """    

    def __init__(self, infection_range: float, recovery_time: int, total_healthcare_capacity: int):
        """
        The constructor is responsible for loading the virus statistics from the config file
        """  
        self.infection_range           = infection_range
        self.recovery_time             = recovery_time
        self.total_healthcare_capacity = total_healthcare_capacity
        
    def infect(self, population: Population, frame):
        #print(len(population.persons[population.persons[:,index.hospitalized] == 1]))

        #Get the index of all the people who were infected in the previous step
        infected_idx = population.get_all_infected()
        persons = population.get_person()

        #print(len(population.persons[:,index.g_value == 0]))
        #print(population.persons[62][index.g_value])
        infected_counter = 0
        for idx in infected_idx:
            infected_counter += 1
            if(population.get_time_infected(int(idx[0]), frame) >= self.recovery_time):
                population = self.die_or_immune(population,int(idx[0]))
            #print(infected_counter)
            # if(population.get_time_infected(int(idx[0]), frame) >= self.recovery_time):
            #     if(infected_counter >= self.total_healthcare_capacity):
            #         #print(infected_counter)
            #         self.healthcare_facility_full = True 
            #         population = self.die_or_immune(population, int(idx[0]), True)
            #     else:
            #         self.healthcare_facility_full = False
            #         population = self.die_or_immune(population, int(idx[0]), False)
            #     break         
            x_bounds = [persons[int(idx[0])][index.x_axis] - math.sqrt(self.infection_range), persons[int(idx[0])][index.x_axis] + math.sqrt(self.infection_range)]
            y_bounds = [persons[int(idx[0])][index.y_axis] - math.sqrt(self.infection_range), persons[int(idx[0])][index.y_axis] + math.sqrt(self.infection_range)]
            # print(population.get_time_infected(int(idx[0]), frame))
            tmp = self.find_nearby(persons, x_bounds, y_bounds)
            for i in tmp:
                chance = np.random.uniform(low = 0.0001, high = 1)
                if chance < persons[int(i)][index.susceptibility] and persons[int(idx[0])][index.g_value] > 0 :
                    population.persons[int(i)][9] = 1
                    population.set_infected_at(int(i), frame)
                    population.persons[int(idx[0])][index.g_value] -= 1
                    if(len(population.persons[population.persons[:,index.hospitalized] == 1]) < self.total_healthcare_capacity):
                        population.persons[int(i)][index.hospitalized] = 1
                        
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
                                        (persons[:, index.current_state] == 0) &
                                        (persons[:, index.current_state] == 0) &
                                        (persons[:,index.social_distance] == 0)
                                    ]
        # print(selected_rows)
        return selected_rows

    def die_or_immune(self, population: Population, infected_person_idx: int) -> bool:
        """
        [summary]

        Parameters
        ----------
        infected_person_idx         : np.array
            [description]
        healthcare_facility_full    : bool
            [description]

        Returns
        -------
        bool
            [description]
        """ 
        chance = np.random.uniform(low = 0.001, high = 1)
        if population.persons[infected_person_idx][index.hospitalized] == 1: 
            population.persons[infected_person_idx][index.hospitalized] = 3
            if(chance < population.persons[infected_person_idx][index.mortality_rate]):
                population.persons[infected_person_idx][index.current_state] = 3
            else:
                population.persons[infected_person_idx][index.current_state] = 2
        else:
            #print('here')
            if(chance < population.persons[infected_person_idx][index.mortality_rate] + 0.2):
                population.persons[infected_person_idx][index.current_state] = 3
            else:
                population.persons[infected_person_idx][index.current_state] = 2
        return population

        

    
    