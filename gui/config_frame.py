"""
Load Config Window application window for Virussim application, built using Tkinter

Created on 2nd Dec, 2020
@author Yatish Pitta
"""

import tkinter as tk
import tkinter.ttk as ttk

from numpy.core.fromnumeric import resize
import gui.ttk_helper
from gui.ttk_helper import ToolTip
from gui.data_store import DataStore


class SetConfigFrame(ttk.Frame):
    """
    Frame widget for configuring and customizing simulation
    """

    def __init__(self, master=None, height=100, width=70):
        """
        Constructor to set the master frame, height and width

        Parameters
        ----------
        :param master: parent frame
        :param height: height of frame
        :param width: width of frame
        """
        super().__init__(master, height=height, width=width,)
        self.master = master
        self.height = height
        self.width = width
        self.data = DataStore.get_instance()
        self.create_widgets()

    def create_widgets(self):
        """
        Creates slider and button widgets for configuring simulation
        """
        
        # Main label frame to hold widgets
        style = ttk.Style(self)
        style.configure("Bold.TLabel", font=("Helvetica", 19, "bold"))
        label_frame_label = ttk.Label(text="Modify Configuration", style="Bold.TLabel")
        label_frame = ttk.LabelFrame(master=self, labelwidget=label_frame_label, height=self.height * 0.95,
                                    width=self.width * 0.95)

        label_frame.grid(row=0, column=0, pady=self.height * 0.02, padx=(self.width * 0.03, 0))
        label_frame.grid_propagate(0)
        
        # Population value slider
        population_label = ttk.Label(master=label_frame, anchor=tk.E, text='Population:')
        population_label.grid(row=0, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)
        popToolTip = ToolTip(widget = population_label, text = "The size of the population for the simulation")

        population_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = popToolTip))
        population_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = popToolTip))

        population_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=200, to=3000, 
                                    length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:self.data.population_val.set('%d' % int(float(s))))
        population_scale.set(1000)
        population_scale.grid(row=0, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                              pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)

        population_scale_val_label = ttk.Label(label_frame, textvariable=self.data.population_val)
        # population_scale_val_label.place(in_=population_scale, bordermode='outside', x=0, y=0, anchor='s')
        population_scale_val_label.grid(row=0, column=1, columnspan=1, sticky = tk.W)


        # Social distancing value slider
        social_distancing_label = ttk.Label(master=label_frame, text='Social Distancing:')

        social_distancing_label.grid(row=1, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)
        socToolTip = ToolTip(widget = social_distancing_label, text = "The percentage of the total population who will be social distancing")

        social_distancing_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = socToolTip))
        social_distancing_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = socToolTip))

        social_distance_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=100, 
                                         length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:self.data.social_distancing_val.set('%d%%' % int(float(s))))
        social_distance_scale.set(50)
        social_distance_scale.grid(row=1, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                   pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)

        distancing_val_label = ttk.Label(label_frame, textvariable=self.data.social_distancing_val)

        distancing_val_label.grid(row=1, column=1, columnspan=1, sticky = tk.W)

        # Hospital capacity value slider
        hostpital_capacity_label = ttk.Label(master=label_frame, text='Healthcare Capacity:')
        hostpital_capacity_label.grid(row=2, column=0, columnspan=1, sticky = tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)

        hosToolTip = ToolTip(widget = hostpital_capacity_label, 
                    text = "The hospital capacity as a percentage of the population. \nWe found in our research that the hospital capacity is generally a function of the population.")

        hostpital_capacity_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = hosToolTip))
        hostpital_capacity_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = hosToolTip))

        hospital_capacity_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=100,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:self.data.hospital_capacity_val.set('%d%%' % int(float(s))))
        hospital_capacity_scale.set(20)
        hospital_capacity_scale.grid(row=2, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        hospital_capacity_val_label = ttk.Label(label_frame, textvariable=self.data.hospital_capacity_val)

        hospital_capacity_val_label.grid(row=2, column=1, columnspan=1, sticky=tk.W)

        # Recovery time value slider
        recovery_time_label = ttk.Label(master=label_frame, text='Recovery Time:')
        recovery_time_label.grid(row=3, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)

        recoveryToolTip = ToolTip(widget = recovery_time_label, 
                    text = "The time a person needs to recover from the virus in unit of frames. \nThis takes into account both if the person is recovering without medical attention or if they needed hospitalization. \nIn our simulation, 1 day roughly amounts to 5 frames.")

        recovery_time_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = recoveryToolTip))
        recovery_time_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = recoveryToolTip))

        self.data.recovery_time_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=50, to=500,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:self.data.recovery_time_val.set('%d' % int(float(s))))
        self.data.recovery_time_scale.set(120)
        self.data.recovery_time_scale.grid(row=3, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        recovery_time_val_label = ttk.Label(label_frame, textvariable=self.data.recovery_time_val)

        recovery_time_val_label.grid(row = 3, column=1, columnspan=1, sticky=tk.W)

        # R value setter button
        r_value_label = ttk.Label(master=label_frame, text='R value:')
        r_value_label.grid(row=4, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)

        rValueToolTip = ToolTip(widget = r_value_label, 
                    text = "The reproduction rate or the R value of the virus. \nThis is defined as the average number of people an infected person goes on to infect.")

        r_value_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = rValueToolTip))
        r_value_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = rValueToolTip))

        self.data.r_value_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=10,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:self.data.r_val.set('%0.2f' % float(s)))
        self.data.r_value_scale.set(3.00)
        self.data.r_value_scale.grid(row=4, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        r_value_val_label = ttk.Label(label_frame, textvariable=self.data.r_val)

        r_value_val_label.grid(row=4, column=1, columnspan=1, sticky=tk.W)

        # K value setter button
        k_value_label = ttk.Label(master=label_frame,  text='K value:')
        k_value_label.grid(row=5, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)

        kValueToolTip = ToolTip(widget = r_value_label, 
                    text = "The K value of the virus. \nThis is defined as the dispersion rate of the R value of the virus.")

        k_value_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = kValueToolTip))
        k_value_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = kValueToolTip))

        self.data.k_value_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=3,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:self.data.k_val.set('%0.2f' % float(s)))
        self.data.k_value_scale.set(0.1)
        self.data.k_value_scale.grid(row=5, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        k_value_val_label = ttk.Label(label_frame, textvariable=self.data.k_val)

        k_value_val_label.grid(row=5, column=1, columnspan=1, sticky=tk.W)
        

        #Enforce Social Distancing At
        enforce_social_distancing_label = ttk.Label(master=label_frame,  text='Social Distancing Starts:')
        enforce_social_distancing_label.grid(row=6, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)

        enforceSocToolTip = ToolTip(widget = enforce_social_distancing_label, 
                    text = "The time at which the city officials decided to announce the social distancing advisory. \nTo enable or disable social distancing, select the checkbox on the right. \nIn our simulation, 1 day roughly amounts to 5 frames.")

        enforce_social_distancing_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = enforceSocToolTip))
        enforce_social_distancing_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = enforceSocToolTip))

        enforce_social_distancing_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=1000,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:self.data.social_distancing_starting_at_val.set('%d' % int(float(s))))
        enforce_social_distancing_scale.set(200)
        enforce_social_distancing_scale.grid(row=6, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        enforce_social_distancing_val_label = ttk.Label(label_frame, textvariable=self.data.social_distancing_starting_at_val)
        enforce_social_distancing_val_label.grid(row=6, column=1, columnspan=1, sticky=tk.W)

        #Mask Wearing Starts At
        enforce_mask_wearing_label = ttk.Label(master=label_frame,  text='Mask Mandate Starts:')
        enforce_mask_wearing_label.grid(row=7, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)

        enforceMaskToolTip = ToolTip(widget = enforce_mask_wearing_label, 
                    text = "The time at which the city officials decided to announce the mask mandate. \nTo enable or disable mask mandates, select the checkbox on the right. \nIn our simulation, 1 day roughly amounts to 5 frames.")

        enforce_mask_wearing_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = enforceMaskToolTip))
        enforce_mask_wearing_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = enforceMaskToolTip))

        enforce_mask_wearing_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=1000,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:self.data.mask_mandate_starting_at_val.set('%d' % int(float(s))))
        enforce_mask_wearing_scale.set(320)
        enforce_mask_wearing_scale.grid(row=7, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        enforce_mask_wearing_val_label = ttk.Label(label_frame, textvariable=self.data.mask_mandate_starting_at_val)
        enforce_mask_wearing_val_label.grid(row=7, column=1, columnspan=1, sticky=tk.W)

        #Set mask effectiveness
        mask_effectiveness_label = ttk.Label(master=label_frame,  text='Mask Effectiveness:')
        mask_effectiveness_label.grid(row=8, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)

        maskEffToolTip = ToolTip(widget = mask_effectiveness_label, 
                    text = "Set the mask effectiveness in protecting an individual from a virus when they come in contact with an infected person. \nWe take into account 3 types of masks that are commonly used by people: cloth masks, surgical masks, N95 masks")

        mask_effectiveness_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = maskEffToolTip))
        mask_effectiveness_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = maskEffToolTip))

        mask_effectiveness_set_button = ttk.Button(label_frame, text="Set Mask Effectiveness", command=self.openMaskWindow)
        mask_effectiveness_set_button.grid(row=8, column=2, pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3, sticky='we')

        #Set mortality rate
        mortality_rate_label = ttk.Label(master=label_frame,  text='Mortality Rate:')
        mortality_rate_label.grid(row=9, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)

        mortalityRateToolTip = ToolTip(widget = mortality_rate_label, 
                    text = "Set the mortality rate of the virus according to the age group that a person belongs to. \nWe take into account 4 standard age groups while determining the mortality rate: 0-19, 20-49, 50-69, 70+")

        mortality_rate_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = mortalityRateToolTip))
        mortality_rate_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = mortalityRateToolTip))

        mortality_rate_set_button = ttk.Button(label_frame, text="Set Mortality Rate", command=self.openMortalityWindow)
        mortality_rate_set_button.grid(row=9, column=2, pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3, sticky='we')
        
    def openMaskWindow(self): 

        newWindow = tk.Toplevel(self.master) 
        
        newWindow.resizable(width=False, height=False)

        photo = tk.PhotoImage(file = "assets/icon-512.png")
        newWindow.iconphoto(False, photo)
        newWindow.resizable(width=False,height=False)

        window_frame = ttk.LabelFrame(master=newWindow)
        window_frame.grid(row=0,column=0)

        style = ttk.Style(self)
        style.configure("Bold.TLabel", font=("Helvetica", 19, "bold"))
        label_frame_label = ttk.Label(master = window_frame, text="Set Mask Effectiveness", style = "Bold.TLabel")
        label_frame = ttk.LabelFrame(master = window_frame, labelwidget=label_frame_label, height = self.height*2, width = self.width*1)
        label_frame.grid(row = 0, column = 0, columnspan=1, pady=self.height * 0.02, padx=(self.width * 0.03, self.width * 0.03))
        mask_type_header_label = ttk.Label(master=label_frame,  text='Mask Type')
        mask_effectivenss_header_label = ttk.Label(master=label_frame,  text='Mask Effectiveness')
        empty_label_1  = ttk.Label(master=label_frame,  text='        ')
        mask_type_header_label.grid(row = 1, column = 0, columnspan=1, sticky = tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.02)
        empty_label_1.grid(row = 1, column = 1, columnspan=1)
        mask_effectivenss_header_label.grid(row = 1, column = 2, columnspan=1)

        #Cloth Mask
        cloth_mask_effectiveness = ttk.Label(master=label_frame,  text='Cloth Mask:')
        cloth_mask_effectiveness.grid(row = 2, column = 0, columnspan=1, sticky = tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.02)

        cloth_mask_effectiveness_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=100,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:self.data.mask_effectiveness_cloth_mask.set('%d%%' % int(float(s))))
        cloth_mask_effectiveness_scale.set(self.data.get_mask_effectiveness_cloth_mask())
        cloth_mask_effectiveness_scale.grid(row=2, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        cloth_mask_effectiveness_val_label = ttk.Label(label_frame, textvariable=self.data.mask_effectiveness_cloth_mask)
        cloth_mask_effectiveness_val_label.grid(row=2, column=1, columnspan=1, sticky=tk.W)

        #Surgical Mask
        surgical_mask_effectiveness = ttk.Label(master=label_frame,  text='Surgical Mask:')
        surgical_mask_effectiveness.grid(row = 3, column = 0, columnspan=1, sticky = tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.02)

        surgical_mask_effectiveness_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=100,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:self.data.mask_effectiveness_surgical_mask.set('%d%%' % int(float(s))))
        surgical_mask_effectiveness_scale.set(self.data.get_mask_effectiveness_surgical_mask())
        surgical_mask_effectiveness_scale.grid(row=3, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        surgical_mask_effectiveness_val_label = ttk.Label(label_frame, textvariable=self.data.mask_effectiveness_surgical_mask)
        surgical_mask_effectiveness_val_label.grid(row=3, column=1, columnspan=1, sticky=tk.W)

        #N95 Mask
        n95_mask_effectiveness = ttk.Label(master=label_frame,  text='N95 Mask:')
        n95_mask_effectiveness.grid(row = 4, column = 0, columnspan=1, sticky = tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.02)

        n95_mask_effectiveness_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=100,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:self.data.mask_effectiveness_n95_mask.set('%d%%' % int(float(s))))
        n95_mask_effectiveness_scale.set(self.data.get_mask_effectiveness_n95_mask())
        n95_mask_effectiveness_scale.grid(row=4, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        n95_mask_effectiveness_val_label = ttk.Label(label_frame, textvariable=self.data.mask_effectiveness_n95_mask)
        n95_mask_effectiveness_val_label.grid(row=4, column=1, columnspan=1, sticky=tk.W)

    def openMortalityWindow(self): 

        newWindow = tk.Toplevel(self.master) 
        newWindow.resizable(width=False, height=False)

        photo = tk.PhotoImage(file = "assets/icon-512.png")
        newWindow.iconphoto(False, photo)
        newWindow.resizable(width=False,height=False)

        window_frame = ttk.LabelFrame(master=newWindow)
        window_frame.grid(row=0,column=0)

        style = ttk.Style(self)
        style.configure("Bold.TLabel", font=("Helvetica", 19, "bold"))
        label_frame_label = ttk.Label(master = window_frame, text="Set Mortality Rate", style = "Bold.TLabel")
        label_frame = ttk.LabelFrame(master=window_frame, labelwidget=label_frame_label, height = self.height*2, width = self.width*1)
        label_frame.grid(row = 0, column = 0, columnspan=1, pady=self.height * 0.02, padx=(self.width * 0.03, self.width * 0.03))
        mask_type_header_label = ttk.Label(master=label_frame,  text='Age Group')
        mask_effectivenss_header_label = ttk.Label(master=label_frame,  text='Mortality Rate')
        empty_label_1  = ttk.Label(master=label_frame,  text='        ')
        mask_type_header_label.grid(row = 1, column = 0, columnspan=1, sticky = tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.02)
        empty_label_1.grid(row = 1, column = 1, columnspan=1)
        mask_effectivenss_header_label.grid(row = 1, column = 2, columnspan=1)

        #0-19 Age Group
        zeronineteen_mortality_rate = ttk.Label(master=label_frame,  text='0-19:')
        zeronineteen_mortality_rate.grid(row = 2, column = 0, columnspan=1, sticky = tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.02)
        zeronineteen_mortality_rate_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0.001, to=10,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:self.data.mortality_rate_zero_to_nineteen.set('%0.03f%%' % float(s)))
        zeronineteen_mortality_rate_scale.set(self.data.get_mortality_rate_zero_to_nineteen())
        zeronineteen_mortality_rate_scale.grid(row=2, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        zeronineteen_mortality_rate_val_label = ttk.Label(label_frame, textvariable=self.data.mortality_rate_zero_to_nineteen)
        zeronineteen_mortality_rate_val_label.grid(row=2, column=1, columnspan=1, sticky=tk.W)

        #20-49 Age Group
        twentyfortynine_mortality_rate = ttk.Label(master=label_frame,  text='20-49:')
        twentyfortynine_mortality_rate.grid(row = 3, column = 0, columnspan=1, sticky = tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.02)
        twentyfortynine_mortality_rate_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0.001, to=10,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:self.data.mortality_rate_twenty_to_fortynine.set('%0.03f%%' % float(s)))
        twentyfortynine_mortality_rate_scale.set(self.data.get_mortality_rate_twenty_to_fortynine())
        twentyfortynine_mortality_rate_scale.grid(row=3, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        twentyfortynine_mortality_rate_val_label = ttk.Label(label_frame, textvariable=self.data.mortality_rate_twenty_to_fortynine)
        twentyfortynine_mortality_rate_val_label.grid(row=3, column=1, columnspan=1, sticky=tk.W)

        #50-69 Age Group
        fiftysixtynine_mortality_rate = ttk.Label(master=label_frame,  text='50-69:')
        fiftysixtynine_mortality_rate.grid(row = 4, column = 0, columnspan=1, sticky = tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.02)

        fiftysixtynine_mortality_rate_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0.001, to=10,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:self.data.mortality_rate_fifty_to_sixtynine.set('%0.03f%%' % float(s)))
        fiftysixtynine_mortality_rate_scale.set(self.data.get_mortality_rate_fifty_to_sixtynine())
        fiftysixtynine_mortality_rate_scale.grid(row=4, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        fiftysixtynine_mortality_rate_val_label = ttk.Label(label_frame, textvariable=self.data.mortality_rate_fifty_to_sixtynine)
        fiftysixtynine_mortality_rate_val_label.grid(row=4, column=1, columnspan=1, sticky=tk.W)

        #70 > Age Group
        seventyplus_mortality_rate = ttk.Label(master=label_frame,  text='70-100:')
        seventyplus_mortality_rate.grid(row = 5, column = 0, columnspan=1, sticky = tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.02)

        seventyplus_mortality_rate_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0.001, to=10,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:self.data.mortality_rate_seventyplus.set('%0.03f%%' % float(s)))
        seventyplus_mortality_rate_scale.set(self.data.get_mortality_rate_seventyplus())
        seventyplus_mortality_rate_scale.grid(row=5, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        seventyplus_mortality_rate_val_label = ttk.Label(label_frame, textvariable=self.data.mortality_rate_seventyplus)
        seventyplus_mortality_rate_val_label.grid(row=5, column=1, columnspan=1, sticky=tk.W)

    
    def get_population_value(self) -> int:
        """
        Get current value of the population slider
        :return: Population value
        """
        return self.population_var

    def set_popluation_value(self, val: int):
        """
        Sets and updates the population value of the slider
        :param val:
        """
        self.population_var = val

    def get_social_distance_value(self) -> float:
        """
        Get current value of the social distance proportion
        :return: Social distance proportion
        """
        return self.social_distance_var

    def set_social_distance_value(self, val: float):
        """
        Sets and updates the social distance proportion value of the slider
        :param val:
        """
        self.social_distance_var = val

    def get_hospital_capacity_value(self) -> int:
        """
        Get current value of the hospital capacity
        :return: Social distance proportion
        """
        return self.hospital_capacity_var

    def set_hospital_capacity_value(self, val: int):
        """
        Sets and updates the hospital capacity value of the slider
        :param val:
        """
        self.hospital_capacity_var = val

    def get_recovery_time_value(self) -> int:
        """
        Get current value of the recovery time
        :return: Social distance proportion
        """
        return self.recovery_time_var

    def set_recovery_time_value(self, val: int):
        """
        Sets and updates the recovery time value of the slider
        :param val:
        """
        self.recovery_time_var = val

    def get_death_rate_value(self) -> float:
        """
        Get current value of the death rate
        :return: Social distance proportion
        """
        return self.death_rate_var

    def set_death_rate_value(self, val: float):
        """
        Sets and updates the death rate value of the slider
        :param val:
        """
        self.death_rate_var = val

    def get_r_value(self) -> int:
        """
        Get current r value
        :return: Social distance proportion
        """
        return self.r_val

    def set_r_value(self, val: int):
        """
        Sets and updates the r value of the slider
        :param val:
        """
        self.r_val = val

    def get_k_value(self) -> float:
        """
        Get current k value
        :return: Social distance proportion
        """
        return self.k_val

    def set_k_value(self, val: float):
        """
        Sets and updates the k value of the slider
        :param val:
        """
        self.k_val = val

    def enter(self, event, tooltip):
            tooltip.showtip()

    def leave(self, event, tooltip):
            tooltip.hidetip()