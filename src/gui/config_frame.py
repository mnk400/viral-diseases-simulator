"""
Load Config Window application window for Virussim application, built using Tkinter

Created on 2nd Dec, 2020
@author Yatish Pitta
"""

import tkinter as tk
import tkinter.ttk as ttk
import ttk_helper
from ttk_helper import ToolTip


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
        super().__init__(master, height=height, width=width)
        self.master = master
        self.height = height
        self.width = width
        self.create_widgets()

    def create_widgets(self):
        """
        Creates slider and button widgets for configuring simulation
        """
        # Main label frame to hold widgets
        style = ttk.Style()
        style.configure("Bold.TLabel", font=("Helvetica", 19, "bold"))
        label_frame_label = ttk.Label(text="Modify Configuration", style="Bold.TLabel")
        label_frame = ttk.LabelFrame(master=self, labelwidget=label_frame_label, height=self.height * 0.95,
                                    width=self.width * 0.95)
        #, font="helvetica 24 bold", background="#ECECEC" text="Modify Configuration"
        label_frame.grid(row=0, column=0, pady=self.height * 0.02)
        label_frame.grid_propagate(0)
        
        # Population value slider
        population_label = ttk.Label(master=label_frame, anchor=tk.E, text='Population:', font="helvetica 11")
        population_label.grid(row=0, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.02)
        toolTip = ttk_helper.ToolTip(widget = population_label)
        def enter(event):
            toolTip.showtip("The size of the population for the simulation")
        def leave(event):
            toolTip.hidetip()
        population_label.bind("<Enter>", enter)
        population_label.bind("<Leave>", leave)

        population_scale_val = tk.StringVar()
        population_scale_val.set('1000')

        population_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=200, to=3000, 
                                    length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:population_scale_val.set('%d' % int(float(s))))
        population_scale.set(1000)
        population_scale.grid(row=0, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                              pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=3)

        population_scale_val_label = ttk.Label(label_frame, textvariable=population_scale_val, font="helvetica 11")
        # population_scale_val_label.place(in_=population_scale, bordermode='outside', x=0, y=0, anchor='s')
        population_scale_val_label.grid(row=0, column=1, columnspan=1, sticky = tk.W)


        # Social distancing value slider
        social_distancing_label = ttk.Label(master=label_frame, text='Social Distancing:', font="helvetica 11")
        # social_distancing_label.grid(row=1, column=0, padx=float(label_frame.winfo_reqwidth()) * 0.025,
        #             pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=1)
        social_distancing_label.grid(row=1, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.02)

        social_distancing_val = tk.StringVar()
        social_distancing_val.set('50%')

        social_distance_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=100, 
                                         length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:social_distancing_val.set('%d%%' % int(float(s))))
        social_distance_scale.set(50)
        social_distance_scale.grid(row=1, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                   pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=3)

        distancing_val_label = ttk.Label(label_frame, textvariable=social_distancing_val, font="helvetica 11")
        # distancing_val_label.place(in_=social_distance_scale, bordermode='outside', x=0, y=0, anchor='s')
        distancing_val_label.grid(row=1, column=1, columnspan=1, sticky = tk.W)

        # Hospital capacity value slider
        hostpital_capacity_label = ttk.Label(master=label_frame, text='Hospital Capacity:', font="helvetica 11")
        hostpital_capacity_label.grid(row=2, column=0, columnspan=1, sticky = tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.02)

        hostpital_capacity_val = tk.StringVar()
        hostpital_capacity_val.set('20%')

        hospital_capacity_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=100,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:hostpital_capacity_val.set('%d%%' % int(float(s))))
        hospital_capacity_scale.set(20)
        hospital_capacity_scale.grid(row=2, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=3)
        
        hospital_capacity_val_label = ttk.Label(label_frame, textvariable=hostpital_capacity_val, font="helvetica 11")
        # hostpital_capacity_val_label.place(in_=hospital_capacity_scale, bordermode='outside', x=0, y=0, anchor='s')
        hospital_capacity_val_label.grid(row=2, column=1, columnspan=1, sticky=tk.W)

        # Recovery time value slider
        recovery_time_label = ttk.Label(master=label_frame, text='Recovery Time:', font="helvetica 11")
        recovery_time_label.grid(row=3, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.02)

        recovery_time_val = tk.StringVar()
        recovery_time_val.set('150')

        recovery_time_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=100, to=500,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:recovery_time_val.set('%d' % int(float(s))))
        recovery_time_scale.set(150)
        recovery_time_scale.grid(row=3, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=3)
        
        recovery_time_val_label = ttk.Label(label_frame, textvariable=recovery_time_val, font="helvetica 11")
        # recovery_time_val_label.place(in_=recovery_time_scale, bordermode='outside', x=0, y=0, anchor='s')
        recovery_time_val_label.grid(row = 3, column=1, columnspan=1, sticky=tk.W)
        # # Death rate value slider
        # self.death_rate_var = tk.DoubleVar()
        # label5 = tk.Label(master=label_frame, anchor='center', text='Death rate')
        # label5.grid(row=4, column=0, padx=float(label_frame.winfo_reqwidth()) * 0.025,
        #             pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=1)
        # label5.grid_propagate(0)
        # death_rate_scale = tk.Scale(master=label_frame, variable=self.death_rate_var, orient='horizontal', from_=0, to=100,
        #                             width=25, sliderlength=100, length=float(label_frame.winfo_reqwidth()) * 0.65)
        # death_rate_scale.grid(row=4, column=1, padx=float(label_frame.winfo_reqwidth()) * 0.05,
        #                       pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=3)
        # death_rate_scale.grid_propagate(0)

        # R value setter button
        r_value_label = ttk.Label(master=label_frame, text='R value:', font="helvetica 11")
        r_value_label.grid(row=4, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.02)

        r_value_val = tk.StringVar()
        r_value_val.set('3.00')

        r_value_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=10,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:r_value_val.set('%0.2f' % float(s)))
        r_value_scale.set(3.00)
        r_value_scale.grid(row=4, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=3)
        
        r_value_val_label = ttk.Label(label_frame, textvariable=r_value_val, font="helvetica 11")
        # r_value_val_label.place(in_=r_value_scale, bordermode='outside', x=0, y=0, anchor='s')
        r_value_val_label.grid(row=4, column=1, columnspan=1, sticky=tk.W)
        # K value setter button
        k_value_label = ttk.Label(master=label_frame,  text='K value:', font="helvetica 11")
        k_value_label.grid(row=5, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.02)

        k_value_val = tk.StringVar()
        k_value_val.set('0.10')

        k_value_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=3,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:k_value_val.set('%0.2f' % float(s)))
        k_value_scale.set(0.1)
        k_value_scale.grid(row=5, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=3)
        
        k_value_val_label = ttk.Label(label_frame, textvariable=k_value_val, font="helvetica 11")
        # k_value_val_label.place(in_=k_value_scale, bordermode='outside', x=0, y=0, anchor='s')
        k_value_val_label.grid(row=5, column=1, columnspan=1, sticky=tk.W)

        #Enforce Social Distancing At
        enforce_social_distancing_label = ttk.Label(master=label_frame,  text='Social Distancing Starts:', font="helvetica 11")
        enforce_social_distancing_label.grid(row=6, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.02)

        enforce_social_distancing_val = tk.StringVar()
        enforce_social_distancing_val.set('200')

        enforce_social_distancing_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=-1, to=1000,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:enforce_social_distancing_val.set('%d' % int(float(s))))
        enforce_social_distancing_scale.set(200)
        enforce_social_distancing_scale.grid(row=6, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=3)
        
        enforce_social_distancing_val_label = ttk.Label(label_frame, textvariable=enforce_social_distancing_val, font="helvetica 11")
        enforce_social_distancing_val_label.grid(row=6, column=1, columnspan=1, sticky=tk.W)

        #Mask Wearing Starts At
    
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


    def convert_to_pixels(self, value, scale, start, extent):
        return ((value - start)/ extent) * (scale.winfo_width()- 10) + 10 / 2