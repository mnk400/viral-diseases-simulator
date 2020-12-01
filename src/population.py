import pandas as pd
import numpy as np


class Population(object):
    """
    This class provides abstraction to all individual person related properties and the dataframe
    holding all persons
    """

    def __init__(self, size):
        """
        Initializes the NumPy array holding all persons with their specific properties
        
        0 - ID:                         An incremental ID uniquely identifying all the individuals              
        1 - age:                        Age of the individuals
        2 - x_axis:                     Refers to the current x position of the individual on the space            
        3 - y_axis:                     Refers to the current y position of the individual on the space   
        4 - x direction:                Refers to the x position of the direction in which the individual is heading  
        5 - y direction:                Refers to the y position of the direction in which the individual is heading 
        6 - speed:                      Speed/offset by which the individual moves on the space
        7 - currently active:           Refers to whether the individual is currently moving towards destination; 0: Random Movement, 1: Towards Destination
        8 - at destination:             Refers to whether the individual is currently at destination; 0: Not at Destination, 1: Destination
        9 - current state:              Current state of the individual; 0: Healthy, 1: Infected, 2: Immune, 3: Dead
        10 - wander_x:                  Once at the destination, the x position to which the individual wanders
        11 - wander_y:                  Once at the destination, the y position to which the individual wanders
        12 - g_value:                   The g value refers to the reproduction of the rate of the individual derived from the k and R value specific to the disease
        13 - susceptibility:            Individual chances of getting infected by the virus, depends on hygiene, and mask
        14 - mortality_rate:            Individual chances of dying due to the virus, depends on age
        15 - mask effectiveness         Stores the effectiveness of the mask that the person is wearing, 0% if not wearing a mask at all
        16 - infected_at                Stores the time unit (in this case a frame) at which someone got infected    
        17 - hospitalized               Stores wheather or not this person is currently hospitalized, was never, or sometime was, 0 - never, 1 - currently is, 3 - sometime was.     
        """

        # Generate the numpy array of population size = size and column size = 12
        self.persons = np.zeros((size, 18))

    def set_age(self, data: list):
        """
        Sets the age of all the persons in the dataframe

        :param data: Column containing all the ages for each person in the population
        :return:
        """
        self.persons[:, 1] = data

    def set_x_axis(self, data: list):
        """
        Sets the x coordinate of each person on the map

        :param data: Column containing all the x coordinates on the space for each person in the population
        :return:
        """
        self.persons[:, 2] = data

    def set_current_state(self, data: list):
        """
        Sets/updates the current state of each person in the population

        :param data: Column containing the updated state for each person in the population
        :return:
        """
        self.persons[:, 8] = data

    def set_y_axis(self, data: list):
        """
        Sets the y coordinate of each person on the map 

        :param data: Column containing all the y coordinates on the space for each person in the population
        :return:
        """
        self.persons[:, 3] = data

    def set_g_value(self, data: list):
        """
        Set the g value for the individual; the g value refers to the reproduction of the rate of the individual
        derived from the k and R value specific to the disease

        :param data: The g value for all the individuals in the population
        """
        self.persons[:, 12] = data

    def set_speed(self, data: list):
        """
        Set the speed for the individual; the speed refers to the offset by which the indivdual moves on the space

        :param data: The speed for all the individuals in the population
        """
        self.persons[:, 6] = data

    def set_at_destination(self, data: list):
        """
        Sets whether the individual is at the destination; 0: Not at Destination, 1: At Destination

        :param data : The value indicating whether the individual is at the destination for all individuals in the population
        """
        self.persons[:, 8] = data

    def set_active(self, data: list):
        """
        Sets whether the individual is currently moving towards destination; 0: Random Movement, 1: Towards Destination

        :param data: The value indicating whether the individual is currently moving towards destination for all individuals in the population
        """
        self.persons[:, 7] = data

    def set_x_dir(self, data):
        """
        Sets the x coordinate of where the person is heading on the space

        :param data: Column containing all the x coordinates of where the person is heading on the space for each person in the population
        """
        self.persons[:, 4] = data

    def set_y_dir(self, data):
        """
        Sets the y coordinate of where the person is heading on the space

        :param data: Column containing all the y coordinates of where the person is heading on the space for each person in the population
        """
        self.persons[:, 5] = data

    def set_infected_at(self, index: int, frame: int):
        """
        Sets the time unit (in this case, a frame) at which a person got infected

        :param index: The id/index of the person for which we need to set the index for
        :param frame: The time frame at which the person got infected
        """
        self.persons[index][16] = frame

    def set_mask_effectiveness(self, data):
        """
        Sets the mask effectiveness for the persons
        :param data:
        """
        self.persons[:, 15] = data

    def get_x_axis(self) -> np.array:
        """
        Returns the current x coordinate of all the persons in the population

        :return: The NumPy array containing the current x coordinate of all the persons in the population
        """
        return self.persons[:, 2]

    def get_y_axis(self) -> np.array:
        """
        Returns the current y coordinate of all the persons in the population

        :return The NumPy array containing the current y coordinate of all the persons in the population
        """
        return self.persons[:, 3]

    def get_current_state(self) -> np.array:
        """
        Returns the current state of all the persons in the population

        :return The current state of all the persons in the population
        """
        return self.persons[:, 9]

    def get_person(self) -> np.ndarray:
        """
        Returns the NumPy array containing all information about all the persons in the population

        :return The NumPy array containing all information about all the persons in the population
        """
        return self.persons

    def get_all_infected(self) -> list:
        """
        Returns the index for all infected individuals in the population

        :return Returns the index of all persons in the population who are infected
        """
        return self.persons[self.persons[:, 9] == 1]

    def get_all_healthy(self) -> list:
        """
        Returns the index for all healthy individuals in the population

        :return Returns the index of all persons in the population who are healthy
        """
        return self.persons[self.persons[:, 9] == 0]

    def get_all_recovered(self) -> list:
        """
        Returns the index for all recovered individuals in the population

        :return Returns the index of all persons in the population who are recovered and are now immune
        """
        return self.persons[self.persons[:, 9] == 2]

    def get_all_dead(self) -> list:
        """
        Returns the index for all dead individuals in the population

        :return Returns the index of all persons in the population who are dead
        """
        return self.persons[self.persons[:, 9] == 3]

    def get_currently_active_info(self) -> np.ndarray:
        """
        Return the column information for all persons' current travel information (whether they have reached their destinations)

        :return The person column array containing current travel information
        """
        return self.persons[:, 7]

    def get_time_infected(self, index: int, current_frame: int) -> int:
        """
        Get the time units (in this case frames) elapsed since a person got infected

        :param index: The index for the person
        :param current_frame: The current frame to get the time elapsed since the person got infected

        :return The elapsed time since person got infected
        """
        return current_frame - self.persons[index][16]

    def get_since_infected_all(self, current_frame: int, recovery_time: int):
        # tmp =  np.array([current_frame]*len(self.persons)) - self.persons[:, 16]
        return self.persons[(current_frame - self.persons[:, 16] > recovery_time)]

    def initialize_id(self, low: int, high: int):
        """
        Initialize the ID for all the individuals in the population

        :param low: Lower bound for ID
        :param high: Upper bound for ID
        """
        ID = list(range(low, high))
        self.persons[:, 0] = ID

    def initialize_ages(self, min_age: int, max_age: int, size: int):
        """
        Initialize the ages of all the individuals in the population. Uses uniform distribution to generate random ages

        :param min_age: Minimum age for the randomly generated ages
        :param max_age: Maximum age for the randomly generated ages
        :param size: Size of the population
        """
        ages = np.int32(np.random.uniform(low=min_age, high=max_age, size=size))
        self.set_age(ages)

    def initialize_positions(self, x_bounds: list, y_bounds: list, size: int):
        """
        Initialize the x positions for all persons in the population

        :param x_bounds: List containing the lower and upper bound for the x axis
        :param y_bounds: List containing the lower and upper bound for the y axis
        :param size: Size of the population
        """
        x_bound_list = np.random.uniform(low=x_bounds[0],
                                         high=x_bounds[1], size=size)
        y_bound_list = np.random.uniform(low=y_bounds[0],
                                         high=y_bounds[1], size=size)
        self.set_x_axis(x_bound_list)
        self.set_y_axis(y_bound_list)

    def initialize_g_value(self, mean: float, std_dev: float, size: int):
        """
        Initialize the g value for all persons in the population. The g value refers to the reproduction of the rate of the individual
        derived from the k and R value specific to the disease 

        :param mean: Mean of the g value to be generated randomly
        :param std_dev: Standard deviation of the g value to be generated randomly
        :param size: Size of the random g value array to be generated
        """
        g_value = np.random.normal(loc=mean, scale=std_dev, size=size)
        g_value[g_value < 0] = 0.00000
        self.set_g_value(g_value.astype(int))

    def initialize_mask_eff(self, size: int):
        """
        Initializing mask effectiveness for all the people in the population. Randomly assigning the mask effectiveness from values 0, 60, 80, 90
        :param size: size of the population
        :return:
        """
        mask_effective_range = [0, 60, 80, 90]
        tmp = np.random.randint(low=0, high=4, size=size)

        tmp[tmp == 0] = mask_effective_range[0]
        tmp[tmp == 1] = mask_effective_range[1]
        tmp[tmp == 2] = mask_effective_range[2]
        tmp[tmp == 3] = mask_effective_range[3]
        self.set_mask_effectiveness(tmp)

    def initialize_susceptibility(self):
        """
        Initialize the susceptibilty to the virus, depends an individual wears a mask, practices good hygiene, and age

        :param mask_effectiveness: Mean of the g value to be generated randomly
        :param hygiene_effectiveness: Standard deviation of the g value to be generated randomly
        :param size: Size of the random g value array to be generated
        """
        tmp = (np.array([100] * len(self.persons)) - self.persons[:, 15]) / 100

        tmp2 = [0.1] * len(self.persons)
        tmp2 = np.multiply(tmp, tmp2)

        self.persons[:, 13] = tmp2

    def initialize_mortality_rate(self, size: int, fatality_rate: dict):
        """
        Initialize the mortality rate of the virus, depends on the age of the person. 
        However, may differ according to healthcare capacity

        :param size: Size of the array to be generated
        :param fatality_rate: Fatality rate risk according to the age group
        """
        for age_groups in fatality_rate.keys():
            age_group_lower_bound = int(age_groups.split("-")[0])
            age_group_upper_bound = int(age_groups.split("-")[1])
            self.persons[:, 14][(self.persons[:, 1] < age_group_lower_bound) &
                                (self.persons[:, 1] > age_group_upper_bound)] = float(fatality_rate[age_groups])


if __name__ == "__main__":
    # p = Person()
    # print(p.persons)
    pass
