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

    def set_destination(self, persons: np.ndarray, destinations: np.ndarray, population: Population) -> np.ndarray:
        """
        Sets destination of the persons in the population who are not currently at their destinations, i.e traveling there

        Parameters
        ----------
        persons : np.ndarray
            The NumPy array containing the details of the persons to be updated
        destinations : np.ndarray
            The NumPy array containing the information regarding each person's destination used for updating

        Returns
        -------
        np.ndarray
            The upated NumPy array with updated values
        """  

        #Get all the persons who are currently traveling to their destinations              
        currently_traveling = np.unique(persons[:, idx.currently_active][persons[:,idx.currently_active] != 0])
        # currently_traveling = np.unique(population.get_currently_active_info()[population.get_currently_active_info() != 0])

        #Update the destinations for all the persons who are currently traveling
        for d in currently_traveling:

            #Get the destination information for each person from the destination array
            destination_x = destinations[:,int((d - 1) * 2)]
            destination_y = destinations[:,int(((d - 1) * 2) + 1)]

            #Using the destination information gathered above, calculate the next step where the person should travel to
            head_x = destination_x - persons[:,idx.x_axis]
            head_y = destination_y - persons[:,idx.y_axis]

            #Update the travel information for each person who are currently traveling to their destination
            persons[:,idx.x_dir][(persons[:,idx.currently_active] == d) &
                            (persons[:,idx.at_destination] == 0)] = head_x[(persons[:,idx.currently_active] == d) &
                                                                (persons[:,idx.at_destination] == 0)]
            persons[:,idx.y_dir][(persons[:,idx.currently_active] == d) &
                            (persons[:,idx.at_destination] == 0)] = head_y[(persons[:,idx.currently_active] == d) &
                                                                (persons[:,idx.at_destination] == 0)]
            
            #Update the speed of the people currently traveling 
            persons[:,idx.speed][(persons[:,idx.currently_active] == d) &
                            (persons[:,idx.at_destination] == 0)] = 0.02
        
        #Return the updated array
        return persons


    def check_at_destination(self, persons: np.ndarray, destinations, wander_factor=1.5, speed = 0.01):
        
        active_dests = np.unique(persons[:,7][(persons[:,7] != 0)])

        #see who is at destination
        for d in active_dests:
            dest_x = destinations[:,int((d - 1) * 2)]
            dest_y = destinations[:,int(((d - 1) * 2) + 1)]

            #see who arrived at destination and filter out who already was there
            at_dest = persons[(np.abs(persons[:,2] - dest_x) < (persons[:,10] * wander_factor)) & 
                                    (np.abs(persons[:,3] - dest_y) < (persons[:,11] * wander_factor)) &
                                    (persons[:,8] == 0)]

            if len(at_dest) > 0:

                #mark those as arrived
                at_dest[:,7] = 0
                at_dest[:,8] = 1

                #insert random headings and speeds for those at destination
                #at_dest = self.update_persons(at_dest, size = len(at_dest), speed = speed,
                #                        heading_update_chance = 1)

                #at_dest[:,6] = 0.001

                #reinsert into self.person.persons
                persons[(np.abs(persons[:,2] - dest_x) < (persons[:,10] * wander_factor)) & 
                           (np.abs(persons[:,3] - dest_y) < (persons[:,11] * wander_factor)) &
                           (persons[:,8] == 0)] = at_dest
                

        return persons

    def keep_at_destination(self, persons: np.ndarray, destinations, wander_factor=1.0):
        print("here")
        active_dests = np.unique(persons[:,11][(persons[:,7] != 0) &
                                                (persons[:,8] == 1)])

        for d in active_dests:
            dest_x = destinations[:,int((d - 1) * 2)][(persons[:,8] == 1) &
                                                        (persons[:,7] == d)]
            dest_y = destinations[:,int(((d - 1) * 2) + 1)][(persons[:,8] == 1) &
                                                            (persons[:,7] == d)]

            #see who is marked as arrived
            arrived = persons[(persons[:,8] == 1) &
                                    (persons[:,7] == d)]

            ids = np.int32(arrived[:,0]) # find unique IDs of arrived persons
            
            #check if there are those out of bounds
            #replace x oob
            #where x larger than destination + wander, AND heading wrong way, set heading negative
            shp = arrived[:,4][arrived[:,2] > (dest_x + (arrived[:,10] * wander_factor))].shape

            arrived[:,4][arrived[:,2] > (dest_x + (arrived[:,10] * wander_factor))] = -np.random.normal(loc = 0.5,
                                                                    scale = 0.5 / 3,
                                                                    size = shp)


            #where x smaller than destination - wander, set heading positive
            shp = arrived[:,4][arrived[:,2] < (dest_x - (arrived[:,10] * wander_factor))].shape
            arrived[:,4][arrived[:,2] < (dest_x - (arrived[:,10] * wander_factor))] = np.random.normal(loc = 0.5,
                                                                scale = 0.5 / 3,
                                                                size = shp)
            #where y larger than destination + wander, set heading negative
            shp = arrived[:,5][arrived[:,3] > (dest_y + (arrived[:,11] * wander_factor))].shape
            arrived[:,5][arrived[:,3] > (dest_y + (arrived[:,11] * wander_factor))] = -np.random.normal(loc = 0.5,
                                                                    scale = 0.5 / 3,
                                                                    size = shp)

            #where y smaller than destination - wander, set heading positive
            shp = arrived[:,5][arrived[:,3] < (dest_y - (arrived[:,11] * wander_factor))].shape
            arrived[:,5][arrived[:,3] < (dest_y - (arrived[:,11] * wander_factor))] = np.random.normal(loc = 0.5,
                                                                scale = 0.5 / 3,
                                                                size = shp)

            #slow speed
            arrived[:,6] = np.random.normal(loc = 0.005,
                                            scale = 0.005 / 3, 
                                            size = arrived[:,6].shape)

            #reinsert into self.person.persons
            persons[(persons[:,8] == 1) &
                        (persons[:,7] == d)] = arrived
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
