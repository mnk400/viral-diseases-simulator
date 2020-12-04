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
        # Main label frame to hold widgets
        label_frame = tk.LabelFrame(master=self, text="Modify Configuration", height=self.height*0.95, width=self.width*0.95)
        label_frame.grid(row=0, column=0, pady=self.height*0.02)
        label_frame.grid_propagate(0)

        # Population value slider
        label1 = tk.Label(master=label_frame, anchor='center', text='Population')
        label1.grid(row=0, column=0, padx=float(label_frame.winfo_reqwidth())*0.025, pady=float(label_frame.winfo_reqheight())*0.025, columnspan=1)
        label1.grid_propagate(0)
        population_scale = tk.Scale(master=label_frame, variable=tk.IntVar(), orient='horizontal', from_=1000, to=100000, width=25, sliderlength=100, length=float(label_frame.winfo_reqwidth())*0.65)
        population_scale.grid(row=0, column=1, padx=float(label_frame.winfo_reqwidth())*0.05, pady=float(label_frame.winfo_reqheight())*0.025, columnspan=3)
        population_scale.grid_propagate(0)

        # Social distancing value slider
        label2 = tk.Label(master=label_frame, anchor='center', text='Social Distancing Ratio')
        label2.grid(row=1, column=0, padx=float(label_frame.winfo_reqwidth())*0.025, pady=float(label_frame.winfo_reqheight())*0.025, columnspan=1)
        label2.grid_propagate(0)
        social_distance_scale = tk.Scale(master=label_frame, variable=tk.DoubleVar(), orient='horizontal', from_=0, to= 1, width=25, sliderlength=100, length=float(label_frame.winfo_reqwidth())*0.65)
        social_distance_scale.grid(row=1, column=1, padx=float(label_frame.winfo_reqwidth())*0.05, pady=float(label_frame.winfo_reqheight())*0.025, columnspan=3)
        social_distance_scale.grid_propagate(0)

        #
        label3 = tk.Label(master=label_frame, anchor='center', text='Hospital capacity')
        label3.grid(row=2, column=0, padx=float(label_frame.winfo_reqwidth())*0.025, pady=float(label_frame.winfo_reqheight())*0.025, columnspan=1)
        label3.grid_propagate(0)
        hospital_capacity_scale = tk.Scale(master=label_frame, variable=tk.DoubleVar(), orient='horizontal', from_=1000, to= 5000, width=25, sliderlength=100, length=float(label_frame.winfo_reqwidth())*0.65)
        hospital_capacity_scale.grid(row=2, column=1, padx=float(label_frame.winfo_reqwidth())*0.05, pady=float(label_frame.winfo_reqheight())*0.025, columnspan=3)
        hospital_capacity_scale.grid_propagate(0)
        #
        label4 = tk.Label(master=label_frame, anchor='center', text='Recovery time')
        label4.grid(row=3, column=0, padx=float(label_frame.winfo_reqwidth())*0.025, pady=float(label_frame.winfo_reqheight())*0.025, columnspan=1)
        label4.grid_propagate(0)
        recovery_time_scale = tk.Scale(master=label_frame, variable=tk.IntVar(), orient='horizontal', from_=1, to=50, width=25, sliderlength=100, length=float(label_frame.winfo_reqwidth())*0.65)
        recovery_time_scale.grid(row=3, column=1, padx=float(label_frame.winfo_reqwidth())*0.05, pady=float(label_frame.winfo_reqheight())*0.025, columnspan=3)
        recovery_time_scale.grid_propagate(0)
        #
        label5 = tk.Label(master=label_frame, anchor='center', text='Death rate')
        label5.grid(row=4, column=0, padx=float(label_frame.winfo_reqwidth())*0.025, pady=float(label_frame.winfo_reqheight())*0.025, columnspan=1)
        label5.grid_propagate(0)
        death_rate_scale = tk.Scale(master=label_frame, variable=tk.IntVar(), orient='horizontal', from_=0, to=100, width=25, sliderlength=100, length=float(label_frame.winfo_reqwidth())*0.65)
        death_rate_scale.grid(row=4, column=1, padx=float(label_frame.winfo_reqwidth())*0.05, pady=float(label_frame.winfo_reqheight())*0.025, columnspan=3)
        death_rate_scale.grid_propagate(0)
        #
        r_val = tk.StringVar()
        r_val_button = tk.Button(master=label_frame, text='Set r value', command='')
        r_val_button.grid(row=5, column=0, padx=float(label_frame.winfo_reqwidth())*0.025, pady=float(label_frame.winfo_reqheight())*0.025, columnspan=1)
        r_val_button.grid_propagate(0)
        r_field = tk.Entry(master=label_frame, textvariable=r_val, width=5)
        r_field.grid(row=5, column=1, padx=float(label_frame.winfo_reqwidth())*0.05, pady=float(label_frame.winfo_reqheight())*0.025, columnspan=3)
        r_field.grid_propagate(0)

        k_val = tk.StringVar()
        k_val_button = tk.Button(master=label_frame, text='Set k value', command='')
        k_val_button.grid(row=6, column=0, padx=float(label_frame.winfo_reqwidth())*0.025, pady=float(label_frame.winfo_reqheight())*0.025, columnspan=1)
        k_val_button.grid_propagate(0)
        k_field = tk.Entry(master=label_frame, textvariable=k_val, width=5)
        k_field.grid(row=6, column=1, padx=float(label_frame.winfo_reqwidth())*0.05, pady=float(label_frame.winfo_reqheight())*0.025, columnspan=3)
        k_field.grid_propagate(0)

        exit_button = tk.Button(master=label_frame, text='Exit', command=self.master.master.master.destroy)
        exit_button.grid(row=7, column=0, padx=float(label_frame.winfo_reqwidth())*0.025, pady=float(label_frame.winfo_reqheight())*0.025, columnspan=4)
        exit_button.grid_propagate(0)