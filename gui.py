#!/usr/bin/env python2

# standard python gui function
from Tkinter import *

import rockpaperscissors

# define a window the game will be viewed in
root = Tk()
root.title ("Mike Patriak's MiniGame Collection")

# create a frame within the window
mainframe = Frame(root, height = 200, width = 500)
# create the window
mainframe.pack_propagate(0)
# pad the borders so content won't touch sides
mainframe.pack(padx = 5, pady = 5)

