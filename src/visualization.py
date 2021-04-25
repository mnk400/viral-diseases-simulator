'''
Created on Jan 29, 2020
@author: manik
'''

from typing import Tuple
from src.population_util import PopulationUtil
from matplotlib import gridspec
import matplotlib.pyplot as plt
import src.person_properties_util as index
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib as mpl
import sys
import networkx as nx
import matplotlib.patches as mpatches


class Visualization():

    def __init__(self, population_util: PopulationUtil,
                 render_mode: bool = False,
                 render_path: str = "render",
                 create_network: bool = False) -> None:
        """
        Constructor to set the population_util, render_mode and path, and
        initialize figure.

        Parameters
        ----------
        :param population_util: PopulationUtil object using which we will run
                                the visualization backend.
        :param render_mode: Toggle to switch to render mode from animation
                            mode.
        :param render_path: Path to where render should be stored.
        """

        self.putil = population_util

        # Disable toolbar
        mpl.rcParams['toolbar'] = 'None'

        # Initialize figure
        self.fig = plt.figure(figsize=(6.5, 7.5))
        self.fig.canvas.set_window_title('Simulation')

        # Initialize 3 subplots
        spec = gridspec.GridSpec(ncols=1, nrows=3, height_ratios=[2, 1, 0.5])
        self.scatter = self.fig.add_subplot(spec[0])
        self.line_graph = self.fig.add_subplot(spec[1])
        self.text_info = self.fig.add_subplot(spec[2])

        # Set X and Y limits and other settings on subplots
        self.scatter.set_xlim(self.putil.x_bounds[0], self.putil.x_bounds[1])
        self.scatter.set_ylim(self.putil.y_bounds[0], self.putil.y_bounds[1])
        self.line_graph.set_xlim(0, 1000)
        self.line_graph.set_ylim(0, self.putil.size)
        self.scatter.axis('off')
        self.text_info.axis('off')

        # Initialize the animation
        self.ani = FuncAnimation(self.fig, self.update, interval=5,
                                 init_func=self.setup_plot, blit=False)

        # If render mode, reinitialize.
        if render_mode is True:
            self.ani = FuncAnimation(self.fig, self.update, interval=5,
                                     frames=1000, init_func=self.setup_plot,
                                     blit=False)
            render_path = render_path + "/render.mp4"
            print("Rendering to " + render_path, file=sys.stdout)
            self.ani.save(render_path, fps=30, dpi=120)
            print("Render Completed", file=sys.stdout)
        # Show animation.
        else:
            plt.show()
            if create_network:
                # Create a digraph showing the infection spread
                fig = plt.figure()
                graph = nx.Graph()
                color_map = []
                size_map = []

                # Label Patches
                red_patch = mpatches.Patch(color='red',
                                           label='First Infection')
                blue_patch = mpatches.Patch(color='cornflowerblue',
                                            label='Infected But Recovered')
                indigo_patch = mpatches.Patch(color='indigo',
                                              label='Dead')
                orange_patch = mpatches.Patch(color='orange',
                                              label='Currently Infected')
                plt.legend(handles=[red_patch, blue_patch, indigo_patch,
                                    orange_patch])

                # Adding graphs edges
                for i in range(self.putil.size):
                    if self.putil \
                        .population.persons[i, index.infected_by] != i \
                            and self.putil \
                            .population.persons[i, index.infected_by] != -1:
                        if self.putil \
                                .population.persons[i,
                                                    index.current_state] == 2:
                            graph.add_edge(i, self.putil.population
                                           .persons[i, index.infected_by])
                            color_map.append('cornflowerblue')
                            size_map.append(15)
                        elif self.putil \
                                .population.persons[i,
                                                    index.current_state] == 3:
                            graph.add_edge(i, self.putil.population
                                           .persons[i, index.infected_by])
                            color_map.append('indigo')
                            size_map.append(15)
                        else:
                            graph.add_edge(i, self.putil.population
                                           .persons[i, index.infected_by])
                            color_map.append('orange')
                            size_map.append(15)
                    elif self.putil \
                            .population.persons[i, index.infected_by] == i:
                        graph.add_node(i)
                        color_map.append('red')
                        size_map.append(50)

                # Show graph
                nx.draw_spring(graph, node_size=size_map,
                               node_color=color_map, edge_color='darkgray')
                fig.canvas.set_window_title('Infection Tracing Visualization')
                plt.show()

    def setup_plot(self) -> Tuple:
        """
        Method to setup how the initial plot and visualization looks like

        Returns
        -------
        :returns Variables that store plot objects
        """

        # Get all the healthy, immune, infected, and dead people seperately
        healthy_x = self.putil.population.get_all_healthy()[:, index.x_axis]
        healthy_y = self.putil.population.get_all_healthy()[:, index.y_axis]
        infected_x = self.putil.population.get_all_infected()[:, index.x_axis]
        infected_y = self.putil.population.get_all_infected()[:, index.y_axis]
        immune_x = self.putil.population.get_all_recovered()[:, index.x_axis]
        immune_y = self.putil.population.get_all_recovered()[:, index.y_axis]
        dead_x = self.putil.population.get_all_dead()[:, index.x_axis]
        dead_y = self.putil.population.get_all_dead()[:, index.y_axis]
        total_infected = self.putil.size - len(healthy_x)

        # Current healthcare status
        self.healthcare_status = "Normal"

        # Scatter plots to plot people
        self.scatter_1 = self.scatter.scatter(healthy_x, healthy_y, vmin=0,
                                              vmax=1, cmap="jet",
                                              c="lightsteelblue", s=10)
        self.scatter_2 = self.scatter.scatter(infected_x, infected_y, vmin=0,
                                              vmax=1, cmap="jet",
                                              c="indianred", s=10)
        self.scatter_3 = self.scatter.scatter(immune_x, immune_y, vmin=0,
                                              vmax=1, cmap="jet",
                                              c="mediumseagreen", s=10)
        self.scatter_4 = self.scatter.scatter(dead_x, dead_y, vmin=0, vmax=1,
                                              cmap="jet", c="indigo", s=10)
        # Lists for line graph
        self.infected = []
        self.infected_total = []
        self.deaths = []
        self.frames = []
        self.immunes = []
        self.infected.append(len(infected_x))
        self.deaths.append(len(dead_x))
        self.infected_total.append(self.putil.size - len(healthy_x))
        self.immunes.append(len(immune_x))
        self.frames.append(0)

        # Line graph plotting number
        self.total_infected, = self.line_graph.plot(self.frames,
                                                    self.infected_total)
        self.currently_infected, = self.line_graph \
            .plot(self.frames, self.infected, c="indianred",
                  label='Currently Infected')
        self.total_deaths, = self.line_graph.plot(self.frames, self.deaths,
                                                  c="indigo",
                                                  label='Total Dead')
        self.total_immune, = self.line_graph.plot(self.frames, self.immunes,
                                                  c="mediumseagreen",
                                                  label='Total Immune')

        # Code below prints statistics
        if(self.putil.enforce_social_distance_at > 0):
            self.line_graph.plot([self.putil.enforce_social_distance_at] * 2,
                                 [0, self.putil.size], c="gold",
                                 label="Social Distancing")
            self.social_distancing_info = "At frame " + \
                str(self.putil.enforce_social_distance_at)
            self.social_distancing_num = \
                str(int(self.putil.social_distance_per * self.putil.size)) + \
                " or " + str(self.putil.social_distance_per*100)+"%"
        else:
            self.social_distancing_info = ("Disabled")
            self.social_distancing_num = "0 or 0%"

        if(self.putil.enforce_mask_wearing_at > 0):
            self.line_graph.plot([self.putil.enforce_mask_wearing_at]*2,
                                 [0, self.putil.size], c="hotpink",
                                 label="Mask Mandate")
            self.mask_wearing_info = "At frame " + \
                str(self.putil.enforce_mask_wearing_at)
        else:
            self.mask_wearing_info = "Disabled"

        self.line_graph.tick_params(axis="y", direction="in", pad=3)
        self.line_graph.plot([0, 10000],
                             [self.putil.virus.total_healthcare_capacity] * 2,
                             c="silver")
        self.line_graph.get_xaxis().set_visible(False)
        self.line_graph.legend(prop={'size': 8}, loc='upper right')

        self.text_info.text(0, 1, "Statistics", fontsize='large',
                            fontweight='bold')
        text_str = "Frame:\nCurrently Infected:\nHealthy People:\n" + \
                   "Immune People:\nTotal Deaths:\nHealthcare Conditions:"
        self.text_info.text(0, -0.5, text_str)
        text_str = "Population:\nMasks Wearing:\nSocial Distancing:\n" + \
                   "People Distancing:\nTotal Infected:\n"
        self.text_info.text(0.54, -0.5, text_str)

        self.scatter.text(0, 1.06, "Simulation", fontsize='xx-large',
                          fontweight='bold')
        self.text_col1 = self.text_info.text(0.33, -0.5,
                                             "%i \n%i \n%s \n%s \n%s \n%s" %
                                             (0, len(infected_x),
                                              str(len(healthy_x)) + " or 0%",
                                              str(len(immune_x)) + " or 0%",
                                              str(len(dead_x)) + " or 0%",
                                              self.healthcare_status))
        self.text_col2 = self.text_info.text(0.81, -0.5,
                                             "%d \n%s \n%s \n%s \n%s\n" %
                                             (self.putil.size,
                                              self.mask_wearing_info,
                                              self.social_distancing_info,
                                              self.social_distancing_num,
                                              total_infected))

        return self.scatter_1, self.scatter_2, self.scatter_3, \
            self.scatter_4, self.currently_infected, self.total_infected,

    def update(self, frame) -> Tuple:
        """
        Similar to the setup function but this updates the simulation

        Parameters
        ----------
        :param frame: Represents the current frame.

        Returns
        -------
        :returns Variables that store plot objects
        """

        if(frame % 1 == 0):
            # Calling method to move people, and check and infect them and
            # perform other functions.
            self.putil.move(frame)

            # Get all the healthy, immune, infected, and dead people
            # seperately
            healthy_x = self.putil.population \
                .get_all_healthy()[:, index.x_axis]
            healthy_y = self.putil.population \
                .get_all_healthy()[:, index.y_axis]
            infected_x = self.putil.population \
                .get_all_infected()[:, index.x_axis]
            infected_y = self.putil.population \
                .get_all_infected()[:, index.y_axis]
            immune_x = self.putil.population \
                .get_all_recovered()[:, index.x_axis]
            immune_y = self.putil.population \
                .get_all_recovered()[:, index.y_axis]
            dead_x = self.putil.population \
                .get_all_dead()[:, index.x_axis]
            dead_y = self.putil.population \
                .get_all_dead()[:, index.y_axis]
            total_infected = self.putil.size - len(healthy_x)
            currently_infected = len(infected_x)

            # Update healthcare status
            if currently_infected > self.putil.total_healthcare_capacity*3/2:
                self.healthcare_status = "Extreme"
            elif currently_infected > self.putil.total_healthcare_capacity:
                self.healthcare_status = "Worse"
            elif currently_infected > self.putil.total_healthcare_capacity*2/3:
                self.healthcare_status = "Manageable"
            else:
                self.healthcare_status = "Normal"

            # Update Graphs
            data1 = np.c_[healthy_x, healthy_y]
            data2 = np.c_[infected_x, infected_y]
            data3 = np.c_[immune_x, immune_y]
            data4 = np.c_[dead_x, dead_y]

            if frame == self.putil.enforce_mask_wearing_at:
                self.mask_wearing_info = "Active"

            if frame == self.putil.enforce_social_distance_at:
                self.social_distancing_info = "Active"

            if frame % 1000 == 0:
                self.line_graph.set_xlim(0, frame + 1000)

            self.text_col1.set_text("%i \n%i \n%s \n%s \n%s \n%s" %
                                    (frame, len(infected_x),
                                     str(len(healthy_x)) + " or " +
                                     str(round(len(healthy_x) *
                                         100/self.putil.size, 1)) + "%",
                                     str(len(immune_x)) + " or " +
                                     str(round(len(immune_x) *
                                         100/self.putil.size, 1)) + "%",
                                     str(len(dead_x)) + " or " +
                                     str(round(len(dead_x) *
                                         100/self.putil.size, 1)) + "%",
                                     self.healthcare_status))
            self.text_col2.set_text("%s \n%s \n%s \n%s \n%s\n" %
                                    (self.putil.size, self.mask_wearing_info,
                                     self.social_distancing_info,
                                     self.social_distancing_num,
                                     total_infected))
            self.scatter_1.set_offsets(data1)
            self.scatter_2.set_offsets(data2)
            self.scatter_3.set_offsets(data3)
            self.scatter_4.set_offsets(data4)

            self.infected.append(len(infected_x))
            self.infected_total.append(self.putil.size - len(healthy_x))
            self.deaths.append(len(dead_x))
            self.frames.append(frame)
            self.immunes.append(len(immune_x))

            self.currently_infected.set_ydata(self.infected)
            self.currently_infected.set_xdata(self.frames)

            self.total_deaths.set_ydata(self.deaths)
            self.total_deaths.set_xdata(self.frames)

            self.total_immune.set_ydata(self.immunes)
            self.total_immune.set_xdata(self.frames)

        return self.scatter_1, self.scatter_2, self.scatter_3, \
            self.scatter_4, self.currently_infected,


if __name__ == "__main__":
    v = Visualization()
