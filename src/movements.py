'''
Created on Nov 29, 2020
@author: manik
'''
'''
File with classes and code which control how a particular person
will move and to where
'''
from src.population import Population
import pandas as pd
import numpy as np
import src.person_properties_util as idx

class Movement():
    """
    Class providing abstraction into each movement of the population
    """    
    
    def update_persons(self, persons: np.ndarray, size: int, speed: float = 0.1, heading_update_chance: float = 0.02) -> np.ndarray:
        """
        Randomly updates/initializes the destination each person is headed to and corresponding speed randomly

        Parameters
        ----------
        person : np.ndarray
            The NumPy array containing the details of the persons to be updated
        size : int
            The size of the array of the persons to be updated to 
        speed : float, optional
            Mean of the speed to be generated randomly, by default 0.1
        heading_update_chance : float, optional
            The odds of updating the destination of each person, by default 0.02

        Returns
        -------
        np.ndarray
            The upated NumPy array with updated values
        """  

        #For updating the x position 
        #Generate a random array with update chance for each person in the population 
        update = np.random.random(size=(size,))

        #Get the persons in the population who have a lower or equal to chance of getting updated in this epoch
        shp = update[update <= heading_update_chance].shape

        #Update the position for the direction in which they are heading
        persons[:,idx.x_dir][update <= heading_update_chance] = np.random.normal(loc = 0, scale = 1/3, size = shp)

        #For updating the y position, do the same
        update = np.random.random(size=(size,))
        shp = update[update <= heading_update_chance].shape
        persons[:,idx.y_dir][update <= heading_update_chance] = np.random.normal(loc = 0, scale = 1/3, size = shp)
        
        #Update the speed by generating a random normal distribution using the argument speed as the parameter
        update = np.random.random(size=(size,))
        shp = update[update <= heading_update_chance].shape
        persons[:,idx.speed][update <= heading_update_chance] = np.random.normal(loc = speed, scale = speed / 3, size = shp)
        persons[:,idx.speed] = np.clip(persons[:,idx.speed], a_min=0.0005, a_max=0.01)

        #Return the updated array
        return persons

    
    def out_of_bounds(self, persons: np.ndarray, xbounds, ybounds):
        shp = persons[:,4][(persons[:,2] <= xbounds[:,0]) &
                            (persons[:,4] < 0)].shape
        persons[:,4][(persons[:,2] <= xbounds[:,0]) &
                        (persons[:,4] < 0)] = np.clip(np.random.normal(loc = 0.5, 
                                                                            scale = 0.5/3,
                                                                            size = shp),
                                                            a_min = 0.05, a_max = 1)

        shp = persons[:,4][(persons[:,2] >= xbounds[:,1]) &
                                (persons[:,4] > 0)].shape
        persons[:,4][(persons[:,2] >= xbounds[:,1]) &
                        (persons[:,4] > 0)] = np.clip(-np.random.normal(loc = 0.5, 
                                                                            scale = 0.5/3,
                                                                            size = shp),
                                                            a_min = -1, a_max = -0.05)

        #update y heading
        shp = persons[:,5][(persons[:,3] <= ybounds[:,0]) &
                                (persons[:,5] < 0)].shape   
        persons[:,5][(persons[:,3] <= ybounds[:,0]) &
                        (persons[:,5] < 0)] = np.clip(np.random.normal(loc = 0.5, 
                                                                            scale = 0.5/3,
                                                                            size = shp),
                                                            a_min = 0.05, a_max = 1)

        shp = persons[:,5][(persons[:,3] >= ybounds[:,1]) &
                                (persons[:,5] > 0)].shape
        persons[:,5][(persons[:,3] >= ybounds[:,1]) &
                        (persons[:,5] > 0)] = np.clip(-np.random.normal(loc = 0.5, 
                                                                            scale = 0.5/3,
                                                                            size = shp),
                                                            a_min = -1, a_max = -0.05)
        
        return persons

    def update_pop(self, persons):
        
        filter = (persons[:, idx.current_state] != 3) & (persons[:, idx.social_distance] == 0)
        

        #x
        persons[:,2][filter] = persons[:,2][filter] + (persons[:,4][filter] * persons[:,6][filter])
        #y
        persons[:,3][filter] = persons[:,3][filter] + (persons [:,5][filter] * persons[:,6][filter])

        return persons
