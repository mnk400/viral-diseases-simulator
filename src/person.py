import pandas as pd
import numpy as np

class Person(object):
    """
    This class provides abstraction to all individual person related properties and the dataframe
    holding all persons
    """

    def __init__(self):
        """
        Initializes the dataframe holding all persons with their specific properties
        Age:                1 - 100
        x_axis:             Depends on the x bounds of the population
        y_axis:             Depends on the y bounds of the population
        current_state:      0: Healthy, 1: Infected, 2: Immune, 3: Dead
        """        
        self.persons = pd.DataFrame(columns=['age', 'x_axis', 'y_axis', 'current_state', 'next_x_axis', 'next_y_axis', 'g_value'])

    def set_age(self, data : list):
        """
        Sets the age of all the persons in the dataframe 

        Parameters
        ----------
        data : list
            Column containing all the ages for each person in the population
        """        
        self.persons['age'] = data
    
    def set_x_axis(self, data : list):
        """
        Sets the x coordinate of each person on the map 

        Parameters
        ----------
        data : list
            Column containing all the x coordinates on the space for each person in the population
        """   
        self.persons['x_axis'] = data

    def get_x_axis(self) -> list:
        """
        Returns the current x coordinate of all the persons in the population

        Returns
        -------
        list
            The list containing the current x coordinate of all the persons in the population
        """        
        return self.persons['x_axis'].to_numpy()
    
    def get_y_axis(self) -> list:
        """
        Returns the current y coordinate of all the persons in the population

        Returns
        -------
        list
            The list containing the current y coordinate of all the persons in the population
        """ 
        return self.persons['y_axis'].to_numpy()

    def set_y_axis(self, data : list):
        """
        Sets the y coordinate of each person on the map 

        Parameters
        ----------
        data : list
            Column containing all the y coordinates on the space for each person in the population
        """ 
        self.persons['y_axis'] = data

    def get_current_state(self) -> np.array:
        """
        Returns the current state of all the persons in the population

        Returns
        -------
        np.array
            The current state of all the persons in the population
        """     
        return self.persons['current_state'].to_numpy

    def set_current_state(self, data: list):
        """
        Sets/updates the current state of each person in the population

        Parameters
        ----------
        data : list
            Column containing the updated state for each person in the population
        """ 
        self.persons['current_state'] = data

    def get_dataframe(self) -> pd.DataFrame:
        """
        Returns the dataframe containing all information about all the persons in the population

        Returns
        -------
        pd.DataFrame
            The pandas dataframe containing all information about all the persons in the population
        """        
        return self.persons

    def get_all_infected(self) -> list:
        """
        Returns the index for all infected individuals in the persons dataframe

        Returns
        -------
        list
           Returns the index of all persons in the population who are infected
        """        
        return self.persons.index[self.persons['current_state'] == 1].tolist()

    def get_all_healthy(self) -> list:
        """
        Returns the index for all healthy individuals in the persons dataframe

        Returns
        -------
        list
           Returns the index of all persons in the population who are healthy
        """        
        return self.persons.index[self.persons['current_state'] == 0].tolist()
    
    def set_g_value(self, data):
        self.persons['g_value'] = data
    
    def set_next_x_axis(self, data : list):
        """
        Sets the x coordinate of each person on the map 

        Parameters
        ----------
        data : list
            Column containing all the x coordinates on the space for each person in the population
        """   
        self.persons['next_x_axis'] = data
    
    def set_next_y_axis(self, data : list):
        """
        Sets the x coordinate of each person on the map 

        Parameters
        ----------
        data : list
            Column containing all the x coordinates on the space for each person in the population
        """   
        self.persons['next_y_axis'] = data

 

if __name__ == "__main__":
    p = Person()
    print(p.persons)