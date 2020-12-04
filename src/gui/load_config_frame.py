"""
Load Config Window application window for Virussim application, built using Tkinter

Created on 2nd Dec, 2020
@author Yatish Pitta
"""

import tkinter as tk
from tkinter import ttk

class LoadConfigFrame(tk.Frame):
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
        self.create_widgets()

    def create_widgets(self):
        """
        Creates button widgets for loading config data of COVID and Influenza viruses
        """

        # Load Config Data button
        self.load_button = ttk.Button(self)
        self.load_button["text"] = "Load COVID Config Data"
        self.load_button["command"] = "hi there, everyone!"
        self.load_button.pack()

        # Load influenza data button
        self.load_inf_button = ttk.Button(self, text="Load Influenza Config Data",
                              command="#")       
        self.load_inf_button.pack()
