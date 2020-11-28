import random
import numpy as np
from person import Person
from virus_util import Virus

class Population(object):
    """
    Class representing the population 
    """

    #_instance = Population()
    # def getInstance():
    #     return Population._instance

    def __init__(self, size: int, x_bounds: list, y_bounds: list, r: float, k: float):
        self.person = Person() 
        self.size         = size
        self.x_bounds     = x_bounds
        self.y_bounds     = y_bounds
        self.k            = k
        self.r            = r
        self.initialize_persons()

    def initialize_persons(self):
        ages = np.int32(np.random.normal(loc=45, scale= 30, size=self.size))
        x_bound_list = np.random.uniform(low=self.x_bounds[0] + 0.1, 
                                            high=self.x_bounds[1] - 0.1, size=self.size)
        y_bound_list = np.random.uniform(low=self.y_bounds[0] + 0.1, 
                                            high=self.y_bounds[1] - 0.1, size=self.size)
        g_value = np.random.normal(loc=self.r, scale=(1/self.k),size=self.size)
        g_value[g_value<0] = 0.00000
        current_state = np.full(shape = (self.size, 1), fill_value = 0)
        self.person.set_age(ages)
        self.person.set_current_state(current_state)
        self.person.set_x_axis(x_bound_list)
        self.person.set_y_axis(y_bound_list)
        self.person.set_g_value(g_value)

if __name__ == "__main__":
    p = Population(100, [0, 1], [0, 1], 3, 0.5)
    #virus = Virus()
    #print(virus.find_nearby(p.person, [0.2, 0.4], [0.3, 0.5]))
    



            


