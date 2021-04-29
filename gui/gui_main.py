"""
Main application window for Virussim application, built using Tkinter

Created on 2nd Dec, 2020
@author Yatish Pitta
"""

import tkinter as tk
import tkinter.ttk as ttk
from gui.buttons_frame import ButtonsFrame
from gui.config_frame import SetConfigFrame


class Application(ttk.Frame):
    """
    Main application window, inherits Frame from Tkinter.
    """

    def __init__(self, master=None, height=100, width=70):
        """
        Constructor to create the main Frame.

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


def main():
    print("Applicaion Launched")
    # root window widget
    root = tk.Tk()

    photo = tk.PhotoImage(file="assets/icon-512.png")
    root.iconphoto(False, photo)
    root.resizable(width=False, height=False)

    height = 420
    width = 750

    # Main application frame
    app = Application(root, height, width)
    app.master.title('Viral Diseases Simulator')

    # Frame holding configuration frame - left
    frame_1 = ttk.Frame(master=app,
                        height=float(app.winfo_reqheight()),
                        width=float(app.winfo_reqwidth()) * 0.55)

    # Configure simulation frame
    config_frame = SetConfigFrame(master=frame_1,
                                  height=float(frame_1.winfo_reqheight()),
                                  width=float(frame_1.winfo_reqwidth()))
    config_frame.grid(row=0, column=0, columnspan=1)

    # Frame holding main action buttons - right
    frame_2 = tk.Frame(master=app,
                       height=float(app.winfo_reqheight()),
                       width=float(app.winfo_reqwidth()) * 0.45)
    load_config_frame = ButtonsFrame(master=frame_2,
                                     height=float(frame_2.winfo_reqheight()),
                                     width=float(frame_2.winfo_reqwidth()))

    load_config_frame.grid(row=0, column=1, columnspan=1)

    frame_1.pack_propagate(0)
    frame_2.pack_propagate(0)
    frame_1.pack(side='left')
    frame_2.pack(side='right')
    app.mainloop()
