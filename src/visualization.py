from population_util import Population as putil 
import matplotlib.pyplot as plt
from time import sleep
from matplotlib.animation import FuncAnimation

class Visualization():

    def __init__(self):
        self.putil = putil(2000, [0,1], [0,1])

    def update(self):
        self.putil = putil(2000, [0,1], [0,1])
        plt.xlim(self.putil.x_bounds[0] , self.putil.x_bounds[1])
        plt.ylim(self.putil.y_bounds[0] , self.putil.y_bounds[1])
        plt.scatter(self.putil.person.getXAxis(), self.putil.person.getYAxis(), s = 10)
        
    
    def animate(self):
        fig = plt.figure(figsize=(10,10))
        
        for i in range(15):
            plt.clf()
            self.update()
            plt.pause(0.5)
        
        plt.show()
        

if __name__ == "__main__":
    v = Visualization()
    v.animate()