from population_util import PopulationUtil as putil 
import matplotlib.pyplot as plt
import person_properties_util as index
from time import sleep
import numpy as np
from matplotlib.animation import FuncAnimation

class Visualization():

    def __init__(self):
        self.putil = putil(500, [0,1], [0,1], 3, 0.5)
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(self.putil.x_bounds[0] , self.putil.x_bounds[1])
        self.ax.set_ylim(self.putil.y_bounds[0] , self.putil.y_bounds[1])
        self.ani = FuncAnimation(self.fig, self.update, interval=5, 
                                          init_func=self.setup_plot, blit=False)
        #self.ani.save("try.mp4", fps=30, dpi=120)
        plt.show()

    def setup_plot(self):
        self.scat = self.ax.scatter(self.putil.population.get_all_healthy()[:, index.x_axis],
                                        self.putil.population.get_all_healthy()[:, index.y_axis], vmin=0, vmax=1,
                                                cmap="jet", edgecolor="k", s=10)
        self.scat2 = self.ax.scatter(self.putil.population.get_all_infected()[:, index.x_axis],
                                        self.putil.population.get_all_infected()[:, index.y_axis], vmin=0, vmax=1,
                                                cmap="jet", edgecolor="r", s=10)
        return self.scat, self.scat2

    def update(self, i):
        if(i % 1 == 0):    
            self.putil.move()
            data1 = np.c_[self.putil.population.get_all_healthy()[:, index.x_axis],
                                        self.putil.population.get_all_healthy()[:, index.y_axis]]
            data2 = np.c_[self.putil.population.get_all_infected()[:, index.x_axis],
                                        self.putil.population.get_all_infected()[:, index.y_axis]]
            self.scat.set_offsets(data1)
            self.scat2.set_offsets(data2)
        
        return self.scat, self.scat2, 

        

if __name__ == "__main__":
    v = Visualization()
    