import pandas as pd

class Person(object):
    """
    This class is used to hold the properties of an individual in a population
    """

    def __init__(self):
        self.persons = pd.DataFrame(columns=['age', 'x_axis', 'y_axis', 'current_state'])

    def set_age(self, data : list):
        self.persons['age'] = data
    
    def set_x_axis(self, data : list):
        self.persons['x_axis'] = data

    def get_x_axis(self) -> list:
        return self.persons['x_axis'].to_numpy()
    
    def get_y_axis(self) -> list:
        return self.persons['y_axis'].to_numpy()

    def set_y_axis(self, data : list):
        self.persons['y_axis'] = data

    def get_current_state(self):
        return self.persons['current_state'].to_numpy

    def set_current_state(self, data: list):
        self.persons['current_state'] = data

    def get_dataframe(self):
        return self.persons

if __name__ == "__main__":
    p = Person()
    print(p.persons)