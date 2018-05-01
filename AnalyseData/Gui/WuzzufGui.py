"""
WuzzufGui will contain classes for the Gui,
the main frame, containing some Buttons,
each Button moves user to another Frame or
to preview answer.
"""

from tkinter import *


class WuzzufGui:
    root = Tk()
    root.geometry("800x700")
    root.title("Wuzzuf Data Analysis")
    btn = Button
    lbl = Label

"""
Here the Gui implements the Tkinter
Given: MainFrame, Geometry and Title

Inside each [extend] there will be the mainloop().
"""
