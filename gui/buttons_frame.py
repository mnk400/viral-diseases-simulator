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

        self.social_distance_enable = tk.IntVar(0)
        social_distance_check = ttk.Checkbutton(master=label_frame3, text='Enable Social Distancing', variable=self.social_distance_enable)
        social_distance_check.invoke()

        social_distance_check.grid(row=0,column=0,columnspan=1, padx=float(self.label_frame.winfo_reqwidth())*0.10, pady=float(self.label_frame.winfo_reqheight())*0.005, sticky=tk.W)

        self.mask_wearing_enable = tk.IntVar(0)
        mask_wearing_check = ttk.Checkbutton(master=label_frame3, text='Enable Mask Wearing', variable=self.mask_wearing_enable)

        mask_wearing_check.grid(row=1,column=0,columnspan=1, padx=float(self.label_frame.winfo_reqwidth())*0.10, pady=float(self.label_frame.winfo_reqheight())*0.005, sticky=tk.W)
        mask_wearing_check.invoke()

        # Load Config Data button
        self.load_button = ttk.Button(master=self.label_frame, text="Load Covid-19 Data", command="#")
        self.load_button.grid(row=4,column=0,columnspan=1, sticky='ew', padx=(float(self.label_frame.winfo_reqwidth()) * 0.05,float(self.label_frame.winfo_reqwidth()) * 0.205), pady=float(self.label_frame.winfo_reqheight()) * 0.02)

        # Load influenza data button
        self.load_inf_button = ttk.Button(master=self.label_frame, text="Load Influenza Data", command="#")       
        self.load_inf_button.grid(row=5,column=0,columnspan=1, sticky='ew', padx=(float(self.label_frame.winfo_reqwidth()) * 0.05,float(self.label_frame.winfo_reqwidth()) * 0.205), pady=float(self.label_frame.winfo_reqheight()) * 0.02)

        #Start custom sim button
        self.start_sim_button = ttk.Button(master=self.label_frame, text="Start Simulation", command=self.info_window)
        self.start_sim_button.grid(row=6,column=0,columnspan=1, sticky='ew', 
                                    padx=(float(self.label_frame.winfo_reqwidth()) * 0.05,float(self.label_frame.winfo_reqwidth()) * 0.205), 
                                    pady=float(self.label_frame.winfo_reqheight()) * 0.02)
        
    def info_window(self):
        self.newWindow = tk.Toplevel(self.master) 
        self.newWindow.resizable(width=False, height=False)

        photo = tk.PhotoImage(file = "assets\icon-512.png")
        self.newWindow.iconphoto(False, photo)
        self.newWindow.resizable(width=False,height=False)
        
        style = ttk.Style(self)
        window_frame = ttk.LabelFrame(master=self.newWindow)
        window_frame.grid(row=0,column=0)
        style.configure("Bold.TLabel", font=("Helvetica", 19, "bold"))
        label_frame_label = ttk.Label(master = window_frame, text="Run Simulation", style = "Bold.TLabel")
        label_frame_top = ttk.LabelFrame(master = window_frame, labelwidget=label_frame_label, height = self.height*2, width = self.width*2)
        label_frame_top.grid(row = 0, column = 0, columnspan=1, pady=self.height * 0.02, padx=(self.width * 0.03, self.width * 0.03))
        

        if self.simulation_mode.get() == 1:
            initial_label_text = "Rendering for the following settings"
        else:
            initial_label_text = "Simulating for the following settings"

        #~~~~~~~~~~~~~~~~~~ LABELS ~~~~~~~~~~~~~~~
        initial_label = ttk.Label(master=window_frame, text=initial_label_text)

        label_frame = ttk.LabelFrame(master=label_frame_top, labelwidget=initial_label, height = self.height*2, width = self.width*2)
        label_frame.grid(row = 0, column = 0, columnspan=1, pady=self.height * 0.02, padx=(self.width * 0.03, self.width * 0.03))
        
        
        population_label = ttk.Label(master=label_frame,text="Population: ")
        population_label.grid(row=1, column=0, columnspan=1, padx=float(label_frame.winfo_reqwidth()) * 0.02, pady=float(label_frame.winfo_reqheight()) * 0.01, sticky=tk.W)

        r_val_label = ttk.Label(master=label_frame,text="R Value: ")
        r_val_label.grid(row=2, column=0, columnspan=1, padx=float(label_frame.winfo_reqwidth()) * 0.02, pady=float(label_frame.winfo_reqheight()) * 0.01, sticky=tk.W)

        k_val_label = ttk.Label(master=label_frame,text="K Value: ")
        k_val_label.grid(row=3, column=0, columnspan=1, padx=float(label_frame.winfo_reqwidth()) * 0.02, pady=float(label_frame.winfo_reqheight()) * 0.01, sticky=tk.W)

        social_distancing_label = ttk.Label(master=label_frame,text="Social Distancing: ")
        social_distancing_label.grid(row=4, column=0, columnspan=1, padx=float(label_frame.winfo_reqwidth()) * 0.02, pady=float(label_frame.winfo_reqheight()) * 0.01, sticky="wn")

        mask_mandates_label = ttk.Label(master=label_frame,text="Mask Mandate: ")
        mask_mandates_label.grid(row=5, column=0, columnspan=1, padx=float(label_frame.winfo_reqwidth()) * 0.02, pady=float(label_frame.winfo_reqheight()) * 0.01, sticky="wn")

        hospital_capacity_label = ttk.Label(master=label_frame,text="Hospital Capacity: ")
        hospital_capacity_label.grid(row=6, column=0, columnspan=1, padx=float(label_frame.winfo_reqwidth()) * 0.02, pady=float(label_frame.winfo_reqheight()) * 0.01, sticky=tk.W)

        mortality_rate_label = ttk.Label(master=label_frame,text="Mortality Rates: ")
        mortality_rate_label.grid(row=7, column=0, columnspan=1, padx=float(label_frame.winfo_reqwidth()) * 0.02, pady=float(label_frame.winfo_reqheight()) * 0.01, sticky="wn")

        #~~~~~~~~~~~~~~~~~~ LABEL VALUES ~~~~~~~~~~~~~~~~~~
        population_label_val = ttk.Label(master=label_frame,text=str(self.data.get_population_val()) + " people.")
        population_label_val.grid(row=1, column=1, columnspan=1, padx=float(label_frame.winfo_reqwidth()) * 0.02, pady=float(label_frame.winfo_reqheight()) * 0.01, sticky=tk.W)

        r_val_label_val = ttk.Label(master=label_frame,text=self.data.get_r_val())
        r_val_label_val.grid(row=2, column=1, columnspan=1, padx=float(label_frame.winfo_reqwidth()) * 0.02, pady=float(label_frame.winfo_reqheight()) * 0.01, sticky=tk.W)

        k_val_label_val = ttk.Label(master=label_frame,text=self.data.get_k_val())
        k_val_label_val.grid(row=3, column=1, columnspan=1, padx=float(label_frame.winfo_reqwidth()) * 0.02, pady=float(label_frame.winfo_reqheight()) * 0.01, sticky=tk.W)
        
        if self.social_distance_enable.get() == 0:
            social_distancing_string = "Disabled"
        else:
            social_distancing_string = str(self.data.get_social_distancing_val()) +"% of people will socially distance.\nStarting at frame " + str(self.data.get_social_distancing_starting_at_val()) + "." 
        
        social_distancing_label_val = ttk.Label(master=label_frame,text=social_distancing_string)
        social_distancing_label_val.grid(row=4, column=1, columnspan=1, padx=float(label_frame.winfo_reqwidth()) * 0.02, pady=float(label_frame.winfo_reqheight()) * 0.01, sticky=tk.W)
        
        if self.mask_wearing_enable.get() == 0:
            mask_string = "Disabled"
        else:
            mask_string = ("Mask Mandate will start at " + str(self.data.get_mask_mandate_starting_at_val()) + " with\nthe following mask effectiveness:" + 
                        "\nCloth Mask: " + str(self.data.get_mask_effectiveness_cloth_mask()) + "% \nSurgical Mask: " + str(self.data.get_mask_effectiveness_surgical_mask()) +
                        "% \nN96 Mask: " + str(self.data.get_mask_effectiveness_n95_mask()) + "%")
                    
        mask_mandates_label_val = ttk.Label(master=label_frame,text=mask_string)
        mask_mandates_label_val.grid(row=5, column=1, columnspan=1, padx=float(label_frame.winfo_reqwidth()) * 0.02, pady=float(label_frame.winfo_reqheight()) * 0.01, sticky="wn")

        hospital_capacity = int(self.data.get_population_val() * self.data.get_hospital_capacity_val()/100)
        hospital_capacity_label_val = ttk.Label(master=label_frame,text=hospital_capacity)
        hospital_capacity_label_val.grid(row=6, column=1, columnspan=1, padx=float(label_frame.winfo_reqwidth()) * 0.02, pady=float(label_frame.winfo_reqheight()) * 0.01, sticky=tk.W)

        mortality_string = ("Age groups and respective mortality rates,\n0 to 19: " + str(self.data.get_mortality_rate_zero_to_nineteen()) + "% \n20 to 49: " + 
                            str(self.data.get_mortality_rate_twenty_to_fortynine()) + "% \n50 to 69: " + str(self.data.get_mortality_rate_fifty_to_sixtynine()) + 
                            "% \n>=70: " + str(self.data.get_mortality_rate_seventyplus()) + "%")
        mortality_rate_label_val = ttk.Label(master=label_frame,text=mortality_string)
        mortality_rate_label_val.grid(row=7, column=1, columnspan=1, padx=float(label_frame.winfo_reqwidth()) * 0.02, pady=float(label_frame.winfo_reqheight()) * 0.01, sticky="wn")

        self.start_sim_button = ttk.Button(master=label_frame, text="Start", command=self.start)
        self.start_sim_button.grid(row=8,column=0,columnspan=2, sticky='ew', 
                                    padx=(float(self.label_frame.winfo_reqwidth()) * 0.05,float(self.label_frame.winfo_reqwidth()) * 0.05), 
                                    pady=float(self.label_frame.winfo_reqheight()) * 0.02)

    def test_print(self):
        print("population" + self.data.population_val.get())
        print("SD" + self.data.social_distancing_val.get())
        print("HC" + self.data.hospital_capacity_val.get())
        print("RT" + self.data.recovery_time_val.get())
        print("R" + self.data.r_val.get())
        print("K" + self.data.k_val.get())
        print("HC" + self.data.social_distancing_starting_at_val.get())
        print("HC" + self.data.mask_mandate_starting_at_val.get())

    def start(self):
        self.start_sim_button["text"] = "Rendering. Please Wait"
        self.update()
        k               = self.data.get_k_val()
        r               = self.data.get_r_val()
        size            = self.data.get_population_val()
        min_age         = self.config_util.getIntegerValue("people.stats", "min_age")
        max_age         = self.config_util.getIntegerValue("people.stats", "max_age")
        mortality       = self.data.get_all_mortality_rates()
        social_dist_per = self.data.get_social_distancing_val()/100
        infection_range = self.config_util.getFloatValue("virus.stats", "infection_range")
        recovery_time   = self.data.get_recovery_time_val()
        health_cap      = int(size * self.data.get_hospital_capacity_val()/100)
        mask_effect     = self.data.get_all_mask_effectiveness()
        speed           = self.config_util.getFloatValue("people.stats", "speed")

        if self.social_distance_enable.get() == 0:
            enforce_social_distance_at = -1
        else:
            enforce_social_distance_at = self.data.get_social_distancing_starting_at_val()

        if self.mask_wearing_enable.get() == 0:
            enforce_masks_at = -1
        else:
            enforce_masks_at = self.data.get_mask_mandate_starting_at_val()

        p_util = PopulationUtil(r=r, k=k, size=size, min_age=min_age, max_age=max_age,
                    mortality_rate=mortality, infection_range=infection_range, recovery_time=recovery_time,
                    total_healthcare_capacity=health_cap, mask_effectiveness=mask_effect,
                    speed=speed, social_distance_per=social_dist_per,social_distancing_at=enforce_social_distance_at,
                    mask_wearing_at=enforce_masks_at)
        
        if self.simulation_mode.get() == 2:
            self.newWindow.destroy()
            Visualization(p_util, render_mode=False)
        else:
            Visualization(p_util, render_mode=True)
        
        if self.simulation_mode.get() == 1:
            self.start_sim_button["text"] = "Done Rendering."