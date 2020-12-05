"""
Main application window for Virussim application, built using Tkinter

Created on 2nd Dec, 2020
@author Yatish Pitta
"""

import tkinter as tk
import tkinter.ttk as ttk
from load_config_frame import LoadConfigFrame
from sim_command_frame import SimCommandFrame
from config_frame import SetConfigFrame


class Application(ttk.Frame):
    """
    Main application window, inherits Frame from Tkinter
    """

    def __init__(self, master=None, height=100, width=70):
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
        self.pack_propagate(0)

if __name__ == '__main__':
    # root window widget
    root = tk.Tk()
    height = root.winfo_screenheight() * 0.6
    width = root.winfo_screenwidth() * 0.4

    # Main application frame
    app = Application(root, height, width)
    app.master.title('COVID SIM')

    # Frame holding configuration frame - left
    action_frame = ttk.Frame(master=app, height=float(app.winfo_reqheight()), width=float(app.winfo_reqwidth()) * 2 / 3)
    # Configure simulation frame
    config_frame = SetConfigFrame(master=action_frame, height=float(action_frame.winfo_reqheight()),
                                  width=float(action_frame.winfo_reqwidth()))
    config_frame.pack()
    config_frame.pack_propagate(0)

    # Frame holding main action buttons - right
    action_frame1 = ttk.Frame(master=app, height=float(app.winfo_reqheight()), width=float(app.winfo_reqwidth()) * 1 / 3)
    label_frame_label = ttk.Label(text="", style="Bold.TLabel")
    label_frame = ttk.LabelFrame(master=action_frame1, labelwidget=label_frame_label, height=(height / 2) * 0.95,
                                    width=float(action_frame1.winfo_reqwidth() * 0.95))
    #, font="helvetica 24 bold", background="#ECECEC" text="Modify Configuration"
    label_frame.grid(row=0, column=0, pady=(height / 2) * 0.02)
    label_frame.grid_propagate(0)
    load_config_frame = LoadConfigFrame(master=label_frame, height=height / 2,
                                        width=float(action_frame1.winfo_reqwidth()))
    sim_command_frame = SimCommandFrame(master=label_frame, height=height / 2,
                                        width=float(action_frame1.winfo_reqwidth()))
    load_config_frame.pack(side='bottom')
    sim_command_frame.pack(side='bottom')
    load_config_frame.pack_propagate(0)
    sim_command_frame.pack_propagate(0)

    action_frame.pack_propagate(0)
    action_frame1.pack_propagate(0)
    action_frame.pack(side='left')
    action_frame1.pack(side='right')
    app.mainloop()
