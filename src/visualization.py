from population_util import Population as putil 
import matplotlib.pyplot as plt
from time import sleep
import numpy as np
from matplotlib.animation import FuncAnimation

class Visualization():

    def __init__(self):
        self.putil = putil(2000, [0,1], [0,1], 3, 0.5)
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(self.putil.x_bounds[0] , self.putil.x_bounds[1])
        self.ax.set_ylim(self.putil.y_bounds[0] , self.putil.y_bounds[1])
        self.ani = FuncAnimation(self.fig, self.update, interval=5, 
                                          init_func=self.setup_plot, blit=False)
        #self.ani.save("try.mp4", fps=30, dpi=120)
        plt.show()

    def setup_plot(self):
        self.scat = self.ax.scatter(self.putil.person.get_dataframe().loc[self.putil.person.get_all_healthy()]['x_axis'], self.putil.person.get_dataframe().loc[self.putil.person.get_all_healthy()]['y_axis'])
        #self.scat2 = self.ax.scatter(self.putil.person.get_dataframe().loc[self.putil.person.get_all_infected()]['x_axis'], self.putil.person.get_dataframe().loc[self.putil.person.get_all_infected()]['y_axis'], s = 10, color = 'red')
        return self.scat

    def update(self, i):
        if(i % 50 == 0):    
            self.putil.move()
            data1 = np.c_[self.putil.person.get_dataframe().loc[self.putil.person.get_all_healthy()]['x_axis'],  self.putil.person.get_dataframe().loc[self.putil.person.get_all_healthy()]['y_axis']]
            self.scat.set_offsets(data1)
        # self.scat.set_offsets([self.putil.person.get_dataframe().loc[self.putil.person.get_all_healthy()]['x_axis'], self.putil.person.get_dataframe().loc[self.putil.person.get_all_healthy()]['y_axis']])
        #self.ax.set_offset(self.putil.person.get_dataframe().loc[self.putil.person.get_all_infected()]['x_axis'], self.putil.person.get_dataframe().loc[self.putil.person.get_all_infected()]['y_axis'], s = 10, color = 'red')
        return self.scat,

    # def animate(self):
    #     fig = plt.figure(figsize=(10,10))
    #     plt.xlim(self.putil.x_bounds[0] , self.putil.x_bounds[1])
    #     plt.ylim(self.putil.y_bounds[0] , self.putil.y_bounds[1])
    #     scatter1 = plt.scatter(self.putil.person.get_dataframe().loc[self.putil.person.get_all_healthy()]['x_axis'], self.putil.person.get_dataframe().loc[self.putil.person.get_all_healthy()]['y_axis'], s = 10, color = 'gray')
    #     scatter2 = plt.scatter(self.putil.person.get_dataframe().loc[self.putil.person.get_all_infected()]['x_axis'], self.putil.person.get_dataframe().loc[self.putil.person.get_all_infected()]['y_axis'], s = 10, color = 'red')
        
    #     # def update(frame):
    #     #     data1 = np.c_[self.putil.person.get_dataframe().loc[self.putil.person.get_all_healthy()]['x_axis'],  self.putil.person.get_dataframe().loc[self.putil.person.get_all_healthy()]['y_axis']]
    #     #     scatter1.set_offsets(data1)
    #     #     data2 = np.c_[self.putil.person.get_dataframe().loc[self.putil.person.get_all_infected()]['x_axis'],  self.putil.person.get_dataframe().loc[self.putil.person.get_all_infected()]['y_axis']]
    #     #     scatter2.set_offsets(data2)
    #     #     self.putil.move()
    #     #     return scatter1, scatter2

    #     ani = FuncAnimation(fig, func = update, frames=500, interval=33, blit=True)
    #     # for i in range(15):
    #     #     plt.clf()
    #     #     self.update()
    #     #     plt.pause(1)
        
    #     plt.show()
        

if __name__ == "__main__":
    v = Visualization()
    