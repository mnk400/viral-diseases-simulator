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

        label4 = tk.Label(master=self, anchor='center', text='Recovery time', pady=15)
        label4.pack()
        recovery_time_scale = tk.Scale(master=self, variable=tk.IntVar(), sliderlength=150, orient='horizontal', from_=1, to=50)
        recovery_time_scale.pack(expand=True, fill='both')

        label5 = tk.Label(master=self, anchor='center', text='Death rate', pady=15)
        label5.pack()
        death_rate_scale = tk.Scale(master=self, variable=tk.IntVar(), sliderlength=150, orient='horizontal', from_=0, to=100)
        death_rate_scale.pack(expand=True, fill='both')

        val_frame = tk.Frame(master=self, width=self.width)
        val_frame.pack(expand=True, fill='both')
        val_frame.pack_propagate(0)
        label6 = tk.Label(master=val_frame, anchor='center', text='R value - ', padx=10)
        label6.pack(side='right')
        label6.grid(row=0, column=0)
        label6.grid_propagate(0)
        r_val = tk.StringVar()
        r_field = tk.Entry(master=val_frame, textvariable=r_val)
        r_val_button = tk.Button(master=val_frame, text='Set r value', command='', width=3)
        r_field.pack(side='right')
        r_field.grid(row=0, column=1)
        r_field.pack_propagate(0)
        r_val_button.pack(side='right')
        r_val_button.grid(row=0, column=2)
        r_val_button.pack_propagate(0)
