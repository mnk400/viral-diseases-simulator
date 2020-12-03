"""
Load Config Window application window for Virussim application, built using Tkinter

Created on 2nd Dec, 2020
@author Yatish Pitta
"""

import tkinter as tk


class LoadConfigFrame(tk.Frame):

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
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Load COVID Config Data"
        self.hi_there["command"] = "hi there, everyone!"
        self.hi_there.pack(expand=True, fill='both', side="bottom")

        # Load influenza data button
        self.quit = tk.Button(self, text="Load Influenza Config Data", fg="red",
                              command="#")
        self.quit.pack(expand=True, fill='both', side="top")
