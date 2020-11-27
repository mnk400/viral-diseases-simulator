import pandas as pd

class Person(object):
    """
    This class is used to hold the properties of an individual in a population
    """

    def __init__(self):
        self.persons = pd.DataFrame(columns=['age', 'x_axis', 'y_axis', 'current_state'])

    def setAge(self, data : list):
        self.persons['age'] = data
    
    def setXAxis(self, data : list):
        self.persons['x_axis'] = data

    def getXAxis(self) -> list:
        return self.persons['x_axis'].to_numpy()
    
    def getYAxis(self) -> list:
        return self.persons['y_axis'].to_numpy()

    def setYAxis(self, data : list):
        self.persons['y_axis'] = data

if __name__ == "__main__":
    p = Person()
    print(p.persons)