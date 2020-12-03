"""
Main application window for Virussim application, built using Tkinter

Created on 2nd Dec, 2020
@author Yatish Pitta
"""

import tkinter as tk
from gui.load_config_frame import LoadConfigFrame
from gui.sim_command_frame import SimCommandFrame


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

# creates root window
root = tk.Tk()
height = root.winfo_screenheight() / 2
width = root.winfo_screenwidth() / 2
app = Application(root, height, width)


action_frame = tk.Frame(master=app, height=height, width=width*2/3)
action_frame1 = tk.Frame(master=app, height=height, width=width*1/3)
load_config_frame = LoadConfigFrame(master=action_frame1, height=height/2, width=width)
sim_command_frame = SimCommandFrame(master=action_frame1, height=height/2, width=width)
load_config_frame.pack(side='top')
sim_command_frame.pack(side='bottom')
load_config_frame.pack_propagate(0)
sim_command_frame.pack_propagate(0)


action_frame.pack_propagate(0)
action_frame1.pack_propagate(0)
action_frame.pack(side='left')
action_frame1.pack(side='right')
app.mainloop()
