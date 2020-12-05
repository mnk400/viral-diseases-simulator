"""
Main application window for Virussim application, built using Tkinter

Created on 2nd Dec, 2020
@author Yatish Pitta
"""

import tkinter as tk
import tkinter.ttk as ttk
from buttons_frame import ButtonsFrame
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
    height = root.winfo_screenheight() * 0.5
    width = root.winfo_screenwidth() * 0.6

    # Main application frame
    app = Application(root, height, width)
    app.master.title('Virus sim')

    # Frame holding configuration frame - left
    action_frame = ttk.Frame(master=app, height=float(app.winfo_reqheight()), width=float(app.winfo_reqwidth()) * 2 / 3)
    # Configure simulation frame
    config_frame = SetConfigFrame(master=action_frame, height=float(action_frame.winfo_reqheight()),
                                  width=float(action_frame.winfo_reqwidth()))
    config_frame.pack()
    config_frame.pack_propagate(0)

    # Frame holding main action buttons - right
    action_frame1 = tk.Frame(master=app, height=float(app.winfo_reqheight()), width=float(app.winfo_reqwidth()) * 1 / 3)
    load_config_frame = ButtonsFrame(master=action_frame1, height=float(action_frame1.winfo_reqheight()),
                                        width=float(action_frame1.winfo_reqwidth()))

    load_config_frame.pack()

    load_config_frame.pack_propagate(0)

    action_frame.pack_propagate(0)
    action_frame1.pack_propagate(0)
    action_frame.pack(side='left')
    action_frame1.pack(side='right')
    app.mainloop()
