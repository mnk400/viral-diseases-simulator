from pandas.core.tools.numeric import to_numeric
from config_util import ConfigUtil
from person import Person
import numpy as np
import math
import random

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

    def infect(self, persons: Person):

        #Store the persons dataframe in a temporary variable
        tmp_df = persons.get_dataframe()

        #Get the index of all the people who were infected in the previous step
        infected_idx = persons.get_all_infected()
        
        infected_to_be = []
        print("Number of infected: " + str(len(infected_idx)))
        #Get the index of all the people within the infection range of the infected persons
        for idx in infected_idx:
            x_bounds = [tmp_df.loc[idx]['x_axis'] - math.sqrt(self.infection_range), 
                            tmp_df.loc[idx]['x_axis'] + math.sqrt(self.infection_range)]
            y_bounds = [tmp_df.loc[idx]['y_axis'] - math.sqrt(self.infection_range), 
                            tmp_df.loc[idx]['y_axis'] + math.sqrt(self.infection_range)]
            
            #Find the nearby people in the infected person's range
            nearby_idx = self.find_nearby(persons, x_bounds, y_bounds)

            #Check other healthy and infected in the infection range
            healthy_index = []
            infected_index = []       #1 person is already infected
            
            for nearby_people in nearby_idx:
                if tmp_df.loc[nearby_people]['current_state'] == 1:
                    infected_index.append(nearby_people)
                elif tmp_df.loc[nearby_people]['current_state'] == 0:
                    healthy_index.append(nearby_people)


            #effective_g_value = int(np.sum(tmp_df.iloc[infected_index]['g_value'].to_numpy()))
            effective_g_value = 3

            if(len(healthy_index) <= effective_g_value):
                infected_to_be += healthy_index
            elif(len(healthy_index) > effective_g_value):
                infected_to_be += random.sample(healthy_index,effective_g_value)
        
        infected_to_be = set(infected_to_be)
        print("Number of people to infect in this turn : " + str(len(infected_to_be)))
            
        tmp_df.loc[list(infected_to_be), 'current_state'] = 1
        #print(tmp_df.loc[infected_to_be])
        return tmp_df
                
    
    def find_nearby(self, person: Person, x_bounds: list, y_bounds: list) -> list:
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
        tmp_df = person.get_dataframe()
        filter1 = tmp_df['x_axis'].gt(x_bounds[0])
        filter2 = tmp_df['x_axis'].lt(x_bounds[1])
        filter3 = tmp_df['y_axis'].gt(y_bounds[0])
        filter4 = tmp_df['y_axis'].lt(y_bounds[1])
        
        index_list = tmp_df.index[filter1 & filter2 & filter3 & filter4].tolist()       
        return index_list
    