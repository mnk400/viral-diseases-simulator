from population_util import PopulationUtil as putil 
import matplotlib.pyplot as plt
import person_properties_util as index
from time import sleep
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib as mpl

class Visualization():

    def __init__(self):
        self.putil = putil(1000, [0,1], [0,1], 3, 0.1)
        mpl.rcParams['toolbar'] = 'None' 
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(self.putil.x_bounds[0] , self.putil.x_bounds[1])
        self.ax.set_ylim(self.putil.y_bounds[0] , self.putil.y_bounds[1])
        plt.axis('off')
        mpl.rcParams['toolbar'] = 'None' 
        self.ani = FuncAnimation(self.fig, self.update, interval=5, 
                                          init_func=self.setup_plot, blit=False)
        self.ani.save("test.gif", fps=30, dpi=120)
        # plt.show()

    def setup_plot(self):
        healthy_x = self.putil.population.get_all_healthy()[:, index.x_axis]
        healthy_y = self.putil.population.get_all_healthy()[:, index.y_axis]
        infected_x = self.putil.population.get_all_infected()[:, index.x_axis]
        infected_y = self.putil.population.get_all_infected()[:, index.y_axis]
        immune_x = self.putil.population.get_all_recovered()[:, index.x_axis]
        immune_y = self.putil.population.get_all_recovered()[:, index.y_axis]
        dead_x = self.putil.population.get_all_dead()[:, index.x_axis]
        dead_y = self.putil.population.get_all_dead()[:, index.y_axis]

        currently_hospitalized = len(self.putil.population.persons[self.putil.population.persons[:,index.hospitalized] == 1])

        self.text = self.ax.text(0, 1.02, "Healthy: %i Infected: %i Immune: %i Dead: %i Hospitalized: %s" % (len(healthy_x),len(infected_x),len(immune_x),len(dead_x),currently_hospitalized))
        self.scat = self.ax.scatter(healthy_x,
                                        healthy_y, vmin=0, vmax=1,
                                                cmap="jet", c="lightsteelblue", s=10)
        self.scat2 = self.ax.scatter(infected_x,
                                        infected_y, vmin=0, vmax=1,
                                                cmap="jet", c="indianred", s=10)
        self.scat3 = self.ax.scatter(immune_x,
                                        immune_y, vmin=0, vmax=1,
                                                cmap="jet", c="mediumseagreen", s=10)
        self.scat4 = self.ax.scatter(dead_x,
                                        dead_y, vmin=0, vmax=1,
                                                cmap="jet", c="indigo", s=10)
        return self.scat, self.scat2, self.scat3, self.scat4

    def update(self, frame):
        if(frame % 1 == 0):    
            self.putil.move(frame)
            
            healthy_x = self.putil.population.get_all_healthy()[:, index.x_axis]
            healthy_y = self.putil.population.get_all_healthy()[:, index.y_axis]
            infected_x = self.putil.population.get_all_infected()[:, index.x_axis]
            infected_y = self.putil.population.get_all_infected()[:, index.y_axis]
            immune_x = self.putil.population.get_all_recovered()[:, index.x_axis]
            immune_y = self.putil.population.get_all_recovered()[:, index.y_axis]
            dead_x = self.putil.population.get_all_dead()[:, index.x_axis]
            dead_y = self.putil.population.get_all_dead()[:, index.y_axis]
            currently_hospitalized = len(self.putil.population.persons[self.putil.population.persons[:,index.hospitalized] == 1])

            data1 = np.c_[healthy_x,healthy_y]
            data2 = np.c_[infected_x,infected_y]
            data3 = np.c_[immune_x,immune_y]
            data4 = np.c_[dead_x,dead_y]
            self.text.set_text("Healthy: %i Infected: %i Immune: %i Dead: %i Hospitalized: %s" % (len(healthy_x),len(infected_x),len(immune_x),len(dead_x),currently_hospitalized))
            self.scat.set_offsets(data1)
            self.scat2.set_offsets(data2)
            self.scat3.set_offsets(data3)
            self.scat4.set_offsets(data4)
        
        return self.scat, self.scat2, self.scat3, self.scat4

        

if __name__ == "__main__":
    v = Visualization()
    