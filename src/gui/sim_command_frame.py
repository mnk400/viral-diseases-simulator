"""
Simulator Command Window for Virussim application, built using Tkinter

Created on 2nd Dec, 2020
@author Yatish Pitta
"""

import tkinter as tk
from tkinter import ttk


class SimCommandFrame(tk.Frame):
    """
    Sim Command Frame contains action buttons to start render mode and start virus simulation
    """

    def __init__(self, master=None, height=100, width=100):
        """
        Constructor to initialize height, width and set master frame

        Parameters
        ----------
        :param master: master frame
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
        Creates the Render Mode and View Simulation buttons
        """
        self.my_var = tk.IntVar()
        rb1 = ttk.Radiobutton(self, text='Render Mode', variable=self.my_var, value=5)
        rb2 = ttk.Radiobutton(self, text='Live Simulation', variable=self.my_var, value=10)
        rb1.pack()
        rb2.pack()
        self.start_sim_button = ttk.Button(self, text="Start",
                              command='#')
        self.start_sim_button.pack()
