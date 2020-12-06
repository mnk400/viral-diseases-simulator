"""
Load Config Window application window for Virussim application, built using Tkinter

Created on 2nd Dec, 2020
@author Yatish Pitta
"""

import tkinter as tk
from tkinter import Widget, ttk
import gui.ttk_helper
from gui.ttk_helper import ToolTip
from src.visualization import Visualization
from src.population_util import PopulationUtil
from src.config_util import ConfigUtil
from gui.data_store import DataStore

class ButtonsFrame(ttk.Frame):
    """
    Load Config Frame contains action buttons to load default simulation configuration for COVID and Influenza viruses
    """

    def __init__(self, master=None, height=100, width=100):
        """
        Constructor to set the master frame, height and width

        Parameters
        ----------
        :param master: parent frame
        :param height: height of frame
        :param width: width of frame
        """
        super().__init__(master, height=height, width=width)
        self.master = master
        self.height = height
        self.width = width
        self.data = DataStore.get_instance()
        self.config_util = ConfigUtil("config/config.ini")
        
        
        self.create_widgets()

    def create_widgets(self):
        """
        Creates button widgets for loading config data of COVID and Influenza viruses
        """
        label_frame_label = ttk.Label(text="", style="Bold.TLabel")
        self.label_frame = ttk.LabelFrame(master=self, labelwidget=label_frame_label, height=self.height*0.95,
                                    width=self.width*0.90)
        self.label_frame.grid(row=0, column=0, pady=self.height * 0.02, padx=(0, self.width * 0.06))
        self.label_frame.grid_propagate(0)

        label_frame_label2 = ttk.Label(text="Simulation Mode")
        label_frame2 = ttk.LabelFrame(master=self.label_frame, labelwidget=label_frame_label2, height=float(self.label_frame.winfo_reqheight())/4.6, width=float(self.label_frame.winfo_reqwidth())*0.9)
        label_frame2.grid(row=0, column=0, columnspan=1, sticky='ew', padx=(float(self.label_frame.winfo_reqwidth()) * 0.05,float(self.label_frame.winfo_reqwidth()) * 0.205))
        label_frame2.grid_propagate(0)

        self.simulation_mode = tk.IntVar()
        self.simulation_mode.set(2)
        rb1 = ttk.Radiobutton(master=label_frame2, text='Render Mode', variable=self.simulation_mode, value=1)
        rb2 = ttk.Radiobutton(master=label_frame2, text='Live Simulation', variable=self.simulation_mode, value=2)
        rb1.grid(row=0,column=0,columnspan=1, padx=float(self.label_frame.winfo_reqwidth()) * 0.10, pady=float(self.label_frame.winfo_reqheight())*0.005, sticky=tk.W)
        rb2.grid(row=1,column=0,columnspan=1, padx=float(self.label_frame.winfo_reqwidth()) * 0.10, pady=float(self.label_frame.winfo_reqheight())*0.005, sticky=tk.W)

        label_frame_label3 = ttk.Label(text="Preventive Options")
        label_frame3 = ttk.LabelFrame(master=self.label_frame, labelwidget=label_frame_label3, height=float(self.label_frame.winfo_reqheight())/4.6, width=float(self.label_frame.winfo_reqwidth())*0.9)
        label_frame3.grid(row=1, column=0, columnspan=1, sticky='ew', padx=(float(self.label_frame.winfo_reqwidth()) * 0.05,float(self.label_frame.winfo_reqwidth()) * 0.205))
        label_frame3.grid_propagate(0)

        #social_distance_enable = tk.IntVar()
        social_distance_check = ttk.Checkbutton(master=label_frame3, text='Enable Social Distancing')
        social_distance_check.invoke()

        social_distance_check.grid(row=0,column=0,columnspan=1, padx=float(self.label_frame.winfo_reqwidth())*0.10, pady=float(self.label_frame.winfo_reqheight())*0.005, sticky=tk.W)

        mask_wearing_enable = tk.IntVar()
        mask_wearing_check = ttk.Checkbutton(master=label_frame3, text='Enable Mask Wearing')

        mask_wearing_check.grid(row=1,column=0,columnspan=1, padx=float(self.label_frame.winfo_reqwidth())*0.10, pady=float(self.label_frame.winfo_reqheight())*0.005, sticky=tk.W)
        mask_wearing_check.invoke()

        # Load Config Data button
        self.load_button = ttk.Button(master=self.label_frame, text="Start Covid Simulation", command=self.execute_covid_sim)
        self.load_button.grid(row=4,column=0,columnspan=1, sticky='ew', padx=(float(self.label_frame.winfo_reqwidth()) * 0.05,float(self.label_frame.winfo_reqwidth()) * 0.205), pady=float(self.label_frame.winfo_reqheight()) * 0.02)

        # Load influenza data button
        self.load_inf_button = ttk.Button(master=self.label_frame, text="Start Influenza Simulation", command="#")       
        self.load_inf_button.grid(row=5,column=0,columnspan=1, sticky='ew', padx=(float(self.label_frame.winfo_reqwidth()) * 0.05,float(self.label_frame.winfo_reqwidth()) * 0.205), pady=float(self.label_frame.winfo_reqheight()) * 0.02)

        #Start custom sim button
        self.start_sim_button = ttk.Button(master=self.label_frame, text="Start Custom Simulation", command=self.test_print)
        self.start_sim_button.grid(row=6,column=0,columnspan=1, sticky='ew', 
                                    padx=(float(self.label_frame.winfo_reqwidth()) * 0.05,float(self.label_frame.winfo_reqwidth()) * 0.205), 
                                    pady=float(self.label_frame.winfo_reqheight()) * 0.02)
        
    
    def test_print(self):
        print(self.data.population_val.get())

    def execute_covid_sim(self):
        render_mode = False

        self.k                          = self.config_util.getFloatValue("virus.stats", "k_value")
        self.r                          = self.config_util.getFloatValue("virus.stats", "r_value")
        self.size                       = self.config_util.getIntegerValue("area.stats", "total_population")
        self.min_age                    = self.config_util.getIntegerValue("people.stats", "min_age")
        self.max_age                    = self.config_util.getIntegerValue("people.stats", "min_age")
        self.mortality_rate             = self.config_util.getDictionary("virus.stats", "mortality_rate")
        self.social_distance_per        = self.config_util.getFloatValue("people.stats", "social_distancing_percent")
        self.infection_range            = self.config_util.getFloatValue("virus.stats", "infection_range")
        self.recovery_time              = self.config_util.getFloatValue("virus.stats", "recovery_time")
        self.total_healthcare_capacity  = self.size*(self.config_util.getIntegerValue("area.stats", "healthcare_capacity_ratio")/100)
        self.mask_effectiveness         = self.config_util.getDictionary("virus.stats", "mask_effectiveness")
        self.speed                      = self.config_util.getFloatValue("people.stats", "speed")
        self.enforce_social_distance_at = self.config_util.getIntegerValue("area.stats", "enforce_social_distancing_at")
        self.enforce_mask_wearing_at    = self.config_util.getIntegerValue("area.stats", "enforce_mask_wearing_at")

        if self.simulation_mode.get() == 1:
            print("inside")
            self.rendering_status_label = ttk.Label(master=self.label_frame, text="Rendering. Please Wait.")
            self.rendering_status_label.grid(row=7, column=0, columnspan=1, sticky='ew', 
                                    padx=(float(self.label_frame.winfo_reqwidth()) * 0.05,float(self.label_frame.winfo_reqwidth()) * 0.205), 
                                    pady=float(self.label_frame.winfo_reqheight()) * 0.02)
            self.update()
            render_mode = True
        
        self.population_util = PopulationUtil(k = self.k, r = self.r, min_age = self.min_age, max_age = self.max_age, size = self.size,
                                mortality_rate = self.mortality_rate, infection_range = self.infection_range, recovery_time = self.recovery_time,
                                total_healthcare_capacity = self.total_healthcare_capacity, social_distance_per = self.social_distance_per,
                                mask_effectiveness = self.mask_effectiveness, speed=self.speed, social_distancing_at = self.enforce_social_distance_at,
                                mask_wearing_at = self.enforce_mask_wearing_at)
        self.visualize = Visualization(self.population_util, render_mode = render_mode)
        if self.simulation_mode.get() == 1:
            self.rendering_status_label["text"] = "Done Rendering."
