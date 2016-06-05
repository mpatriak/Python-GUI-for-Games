#!/usr/bin/env python2

# standard python gui function
from Tkinter import *

import rockpaperscissors

# define a window the game will be viewed in
root = Tk()
root.title ("Michal Patriak's MiniGame Collection")

# create a frame within the window
mainframe = Frame(root, height = 200, width = 500)
# create the window
mainframe.pack_propagate(0)
# pad the borders so content won't touch sides
mainframe.pack(padx = 5, pady = 5)

# define an intro to display in the window
intro = Label(mainframe, text = """Welcome to Michal Patriak's MiniGame Collection.
Please select one of the following games to play: """)
# display the intro
intro.pack(side = TOP)

# create a button for rockpaperscissors
rps_button = Button(mainframe, text = "Rock, Paper, Scissors",
                    command = rockpaperscissors.gui)
rps_button.pack()

# create a button for hangman
hm_button = Button(mainframe, text = "Hangman", command = hangman.start)
hm_button.pack()

# create a button for poker dice
pd_button = Button(mainframe, text = "Poker Dice", command = pokerdice.start)
pd_button.pack()

# exit button
exit_button = Button(mainframe, text = "Quit", command = root.destroy)
exit_button.pack(side = BOTTOM)

root.mainloop()
