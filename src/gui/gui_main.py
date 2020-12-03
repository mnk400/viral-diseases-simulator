"""
Main application window for Virussim application, built using Tkinter

Created on 2nd Dec, 2020
@author Yatish Pitta
"""

import tkinter as tk
from gui.action_frame import ActionFrame


class Application(tk.Frame):
    """
    Main application window, inherits Frame from Tkinter
    """

    def __init__(self, master=None, height=100, width=100):
        """
        Constructor to create the main Frame

        Parameters
        ----------
        :param master: master frame
        :param height: height of frame
        :param width: width of frame
        """
        super().__init__(master, height=height, width=width)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        pass


root = tk.Tk()
height = root.winfo_screenheight() / 2
width = root.winfo_screenwidth() / 2
app = Application(root, height, width)
action_frame = ActionFrame(master=app, height=height, width=width/2)
action_frame1 = ActionFrame(master=app, height=height, width=width/2)
action_frame.pack_propagate(0)
action_frame1.pack_propagate(0)
action_frame.pack(side='left')
action_frame1.pack(side='right')
app.mainloop()
