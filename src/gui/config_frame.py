"""
Load Config Window application window for Virussim application, built using Tkinter

Created on 2nd Dec, 2020
@author Yatish Pitta
"""

import tkinter as tk


class SetConfigFrame(tk.Frame):

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
        Creates button widgets for loading config data of COVID and Influenza viruses
        """

        # Load Config Data button
        label1 = tk.Label(master=self, anchor='center', text='Population', pady=15)
        label1.pack()
        population_scale = tk.Scale(master=self, variable=tk.IntVar(), sliderlength=150, orient='horizontal', from_=1000, to=100000)
        population_scale.pack(expand=True, fill='both')

        label2 = tk.Label(master=self, anchor='center', text='Social Distancing Ratio', pady=15)
        label2.pack()
        social_distance_scale = tk.Scale(master=self, variable=tk.DoubleVar(), sliderlength=150, orient='horizontal', from_=0, to= 1)
        social_distance_scale.pack(expand=True, fill='both')

        label3 = tk.Label(master=self, anchor='center', text='Hospital capacity', pady=15)
        label3.pack()
        hospital_capacity_scale = tk.Scale(master=self, variable=tk.DoubleVar(), sliderlength=150, orient='horizontal', from_=1000, to= 5000)
        hospital_capacity_scale.pack(expand=True, fill='both')
