"""
Load Config Window application window for Virussim application, built using Tkinter

Created on 2nd Dec, 2020
@author Yatish Pitta
"""

import tkinter as tk


class SetConfigFrame(tk.Frame):
    """
    Frame widget for configuring and customizing simulation
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
        self.create_widgets()

    def create_widgets(self):
        """
        Creates slider and button widgets for configuring simulation
        """
        # Main label frame to hold widgets
        label_frame = tk.LabelFrame(master=self, text="Modify Configuration", height=self.height * 0.95,
                                    width=self.width * 0.95)
        label_frame.grid(row=0, column=0, pady=self.height * 0.02)
        label_frame.grid_propagate(0)

        # Population value slider
        self.population_var = tk.IntVar()
        label1 = tk.Label(master=label_frame, anchor='center', text='Population')
        label1.grid(row=0, column=0, padx=float(label_frame.winfo_reqwidth()) * 0.025,
                    pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=1)
        label1.grid_propagate(0)
        population_scale = tk.Scale(master=label_frame, variable=self.population_var, orient='horizontal', from_=1000,
                                    to=100000, width=25, sliderlength=100,
                                    length=float(label_frame.winfo_reqwidth()) * 0.65)
        population_scale.grid(row=0, column=1, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                              pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=3)
        population_scale.grid_propagate(0)

        # Social distancing value slider
        self.social_distance_var = tk.DoubleVar()
        label2 = tk.Label(master=label_frame, anchor='center', text='Social Distancing Ratio')
        label2.grid(row=1, column=0, padx=float(label_frame.winfo_reqwidth()) * 0.025,
                    pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=1)
        label2.grid_propagate(0)
        social_distance_scale = tk.Scale(master=label_frame, variable=self.social_distance_var, orient='horizontal', from_=0.00,
                                         to=1.00, width=25, sliderlength=100,
                                         length=float(label_frame.winfo_reqwidth()) * 0.65)
        social_distance_scale.grid(row=1, column=1, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                   pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=3)
        social_distance_scale.grid_propagate(0)

        # Hospital capacity value slider
        self.hospital_capacity_var = tk.IntVar()
        label3 = tk.Label(master=label_frame, anchor='center', text='Hospital capacity')
        label3.grid(row=2, column=0, padx=float(label_frame.winfo_reqwidth()) * 0.025,
                    pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=1)
        label3.grid_propagate(0)
        hospital_capacity_scale = tk.Scale(master=label_frame, variable=self.hospital_capacity_var, orient='horizontal', from_=1000,
                                           to=5000, width=25, sliderlength=100,
                                           length=float(label_frame.winfo_reqwidth()) * 0.65)
        hospital_capacity_scale.grid(row=2, column=1, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=3)
        hospital_capacity_scale.grid_propagate(0)

        # Recovery time value slider
        self.recovery_time_var = tk.IntVar()
        label4 = tk.Label(master=label_frame, anchor='center', text='Recovery time')
        label4.grid(row=3, column=0, padx=float(label_frame.winfo_reqwidth()) * 0.025,
                    pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=1)
        label4.grid_propagate(0)
        recovery_time_scale = tk.Scale(master=label_frame, variable=self.recovery_time_var, orient='horizontal', from_=1, to=50,
                                       width=25, sliderlength=100, length=float(label_frame.winfo_reqwidth()) * 0.65)
        recovery_time_scale.grid(row=3, column=1, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                 pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=3)
        recovery_time_scale.grid_propagate(0)

        # Death rate value slider
        self.death_rate_var = tk.DoubleVar()
        label5 = tk.Label(master=label_frame, anchor='center', text='Death rate')
        label5.grid(row=4, column=0, padx=float(label_frame.winfo_reqwidth()) * 0.025,
                    pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=1)
        label5.grid_propagate(0)
        death_rate_scale = tk.Scale(master=label_frame, variable=self.death_rate_var, orient='horizontal', from_=0, to=100,
                                    width=25, sliderlength=100, length=float(label_frame.winfo_reqwidth()) * 0.65)
        death_rate_scale.grid(row=4, column=1, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                              pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=3)
        death_rate_scale.grid_propagate(0)

        # R value setter button
        self.r_val = tk.IntVar()
        r_val_button = tk.Button(master=label_frame, text='Set r value', command='#')
        r_val_button.grid(row=5, column=0, padx=float(label_frame.winfo_reqwidth()) * 0.025,
                          pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=1)
        r_val_button.grid_propagate(0)
        r_field = tk.Entry(master=label_frame, textvariable=self.r_val, width=5)
        r_field.grid(row=5, column=1, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                     pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=3)
        r_field.grid_propagate(0)

        # K value setter button
        self.k_val = tk.DoubleVar()
        k_val_button = tk.Button(master=label_frame, text='Set k value', command='')
        k_val_button.grid(row=6, column=0, padx=float(label_frame.winfo_reqwidth()) * 0.025,
                          pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=1)
        k_val_button.grid_propagate(0)
        k_field = tk.Entry(master=label_frame, textvariable=self.k_val, width=5)
        k_field.grid(row=6, column=1, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                     pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=3)
        k_field.grid_propagate(0)

        # Exit button
        exit_button = tk.Button(master=label_frame, text='Exit', command=self.master.master.master.destroy)
        exit_button.grid(row=7, column=0, padx=float(label_frame.winfo_reqwidth()) * 0.025,
                         pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=4)
        exit_button.grid_propagate(0)

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

