import random
import numpy as np
from person import Person


class Population(object):
    """
    Class representing the population 
    """

    #_instance = Population()
    # def getInstance():
    #     return Population._instance

    def __init__(self, size: int, x_bounds: list, y_bounds: list):
        self.person = Person() 
        self.size         = size
        self.x_bounds     = x_bounds
        self.y_bounds     = y_bounds
        self.initialize_persons()

    def initialize_persons(self):
        ages = np.int32(np.random.normal(loc=45, scale= 30, size=self.size))
        x_bound_list = np.random.uniform(low=self.x_bounds[0] + 0.1, 
                                            high=self.x_bounds[1] - 0.1, size=self.size)
        y_bound_list = np.random.uniform(low=self.y_bounds[0] + 0.1, 
                                            high=self.y_bounds[1] - 0.1, size=self.size)
        self.person.setAge(ages)
        self.person.setXAxis(x_bound_list)
        self.person.setYAxis(y_bound_list)

if __name__ == "__main__":
    p = Population(100, [0, 1], [0, 1])
    p.initialize_persons()
    print(p.person.persons)



            


