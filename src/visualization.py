from population_util import PopulationUtil as putil 
import matplotlib.pyplot as plt
from time import sleep
import numpy as np
from matplotlib.animation import FuncAnimation

class Visualization():

    def __init__(self):
        self.putil = putil(500, [0,1], [0,1], 3, 0.5)
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(self.putil.x_bounds[0] , self.putil.x_bounds[1])
        self.ax.set_ylim(self.putil.y_bounds[0] , self.putil.y_bounds[1])
        self.ani = FuncAnimation(self.fig, self.update, interval=33, 
                                          init_func=self.setup_plot, blit=False)
        #self.ani.save("try.mp4", fps=30, dpi=120)
        plt.show()

    def setup_plot(self):
        self.scat = self.ax.scatter(self.putil.persons[:,2],
                                        self.putil.persons[:,3], vmin=0, vmax=1,
                                                cmap="jet", edgecolor="k")

        return self.scat

    def update(self, i):
        if(i % 1 == 0):    
            self.putil.move()
            data1 = np.c_[self.putil.persons[:,2],  self.putil.persons[:,3]]
            self.scat.set_offsets(data1)
        
        return self.scat, 

        

if __name__ == "__main__":
    v = Visualization()
    