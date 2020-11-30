'''
File with classes and code which control how a particular person
will move and to where
'''
from person import Person
import pandas as pd
import numpy as np

class Movement():
    """
    Class providing abstraction into each movement of the population
    """    
    
    def move(self, person : Person):

        x = person.get_dataframe()['x_axis'].to_numpy()
        y = person.get_dataframe()['y_axis'].to_numpy()

        x1 = person.get_dataframe()['destination_x'].to_numpy()
        y1 = person.get_dataframe()['destination_y'].to_numpy()

        slope = np.divide((y - y1), (x - x1))

        b = y1 - np.multiply(slope,x1)

        speed = person.get_dataframe()['speed'].to_numpy()

        x = x + speed
        y = np.multiply(slope,x) + b

        person.set_x_axis(x)
        person.set_y_axis(y)
