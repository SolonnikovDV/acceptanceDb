from tkinter import *

class InformationWindow:
    def __init__(self, parent, width, height, x, y, title, resizable=(False, False)):
        self.root = Toplevel(parent)
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        self.root.resizable(resizable[0], resizable[1])