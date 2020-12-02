from src.population_util import PopulationUtil  
from matplotlib import gridspec
import matplotlib.pyplot as plt
import src.person_properties_util as index
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib as mpl

class Visualization():

    def __init__(self, population_util: PopulationUtil):
        self.putil = population_util
        mpl.rcParams['toolbar'] = 'None' 
        self.fig = plt.figure()
        spec = gridspec.GridSpec(ncols=1, nrows=2,height_ratios=[2, 1])
        self.ax = self.fig.add_subplot(spec[0])
        self.ax1 = self.fig.add_subplot(spec[1])
        self.ax.set_xlim(self.putil.x_bounds[0] , self.putil.x_bounds[1])
        self.ax.set_ylim(self.putil.y_bounds[0] , self.putil.y_bounds[1])
        self.ax1.set_xlim(0 , 1000)
        self.ax1.set_ylim(0 , 1000)
        self.ax.axis('off')
        mpl.rcParams['toolbar'] = 'None' 
        self.ani = FuncAnimation(self.fig, self.update, interval=5, 
                                          init_func=self.setup_plot, blit=False)
        #self.ani.save("test.gif", fps=30, dpi=120)
        plt.show()

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

        self.text = self.ax.text(0, 1.02, "Frame: %i Healthy: %i Infected: %i Immune: %i Dead: %i Hospitalized: %s" %(0,len(healthy_x),len(infected_x),len(immune_x),len(dead_x),currently_hospitalized))
        self.text2 = self.ax.text(0,-.04,"Masks Enforced: %s Social Distancing: %s" % (str(self.putil.mask_wearing_enforced),str(self.putil.social_distancing_enforced)))
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
        self.infected       = []
        self.infected_total = []
        self.deaths         = []
        self.frames         = []
        self.immunes        = []
        self.infected.append(len(infected_x))
        self.deaths.append(len(dead_x))
        self.infected_total.append(self.putil.size - len(healthy_x))
        self.immunes.append(len(immune_x))
        self.frames.append(0)
        self.total_infected,     = self.ax1.plot(self.frames, self.infected_total)
        self.currently_infected, = self.ax1.plot(self.frames, self.infected, c="darkgoldenrod", label='Currently Infected')
        self.total_deaths,       = self.ax1.plot(self.frames, self.deaths, c="indianred", label='Total Dead')
        self.total_immune        = self.ax1.plot(self.frames, self.immunes, c="mediumseagreen", label='Total Immune')
        
        if(self.putil.enforce_social_distance_at > 0):
            self.ax1.plot([self.putil.enforce_social_distance_at]*2, [0,self.putil.size],c="gray")

        if(self.putil.enforce_mask_wearing_at > 0):
            self.ax1.plot([self.putil.enforce_mask_wearing_at]*2, [0,self.putil.size],c="gray")

        self.ax1.plot([0,1000],[self.putil.virus.total_healthcare_capacity]*2, c="silver")

        self.ax1.legend()
        return self.scat, self.scat2, self.scat3, self.scat4, self.currently_infected, self.total_infected, 

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
            self.text.set_text("Frame: %i Healthy: %i Infected: %i Immune: %i Dead: %i Hospitalized: %s" % (frame,len(healthy_x),len(infected_x),len(immune_x),len(dead_x),currently_hospitalized))
            self.text2.set_text("Masks Enforced: %s Social Distancing: %s" % (str(self.putil.mask_wearing_enforced),str(self.putil.social_distancing_enforced)))
            self.scat.set_offsets(data1)
            self.scat2.set_offsets(data2)
            self.scat3.set_offsets(data3)
            self.scat4.set_offsets(data4)
   
            self.infected.append(len(infected_x))
            self.infected_total.append(self.putil.size - len(healthy_x))
            self.deaths.append(len(dead_x))
            self.frames.append(frame)
            self.immunes.append(len(immune_x))

            self.currently_infected.set_ydata(self.infected)
            self.currently_infected.set_xdata(self.frames)

            #self.total_infected.set_ydata(self.infected_total)
            #self.total_infected.set_xdata(self.frames)

            self.total_deaths.set_ydata(self.deaths)
            self.total_deaths.set_xdata(self.frames)

            self.total_infected.set_ydata(self.immunes)
            self.total_infected.set_xdata(self.frames)

            
        
        return self.scat, self.scat2, self.scat3, self.scat4, self.currently_infected,

        

if __name__ == "__main__":
    v = Visualization()
    