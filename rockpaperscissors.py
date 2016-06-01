#!/usr/bin/env python2

# Extra modules used
from Tkinter import *
from ttk import *
import random

def gui():
    

    # Set each move to a specific number
    # Once a selection is made by the player,
    # it will be equated to that specific variable.
    rock = 1
    paper = 2
    scissors = 3

    # Text representation of each move
    names = { rock: "Rock", paper: "Paper", scissors: "Scissors" }

    # Game Rules
    rules = { rock: scissors, paper: rock, scissors: paper }

    # Function to print a greeting and start
    # a loop to allow the player to continue
    #playing as many times as they wish
    def start():
        while game():
            pass # Allows the loop to stop when player is done

    def game():
        player = player_choice.get()
        computer = random.randint(1, 3)
        computer_choice.set(names[computer])
        result(player, computer)

    def result(player, computer):
        new_score = 0
        if player == computer:
            result_set.set("Tie game.")
        elif rules[player] == computer:
            result_set.set("Your victory has been assured.")
            new_score = player_score.get()
            new_score += 1
            player_score.set(new_score)
        else:
            result_set.set("The computer laughs as you realize you have been defeated.")
            new_score = computer_score.get()
            new_score += 1
            computer_score.set(new_score)

    # create a game window on top level
    rps_window = Toplevel()
    rps_window.title("Rock, Paper, Scissors")
    player_choice = IntVar()
    computer_choice = StringVar()
    result_set = StringVar()
    player_choice.set(1)
    player_score = IntVar()
    computer_score = IntVar()

    # create a frame for the game
    rps_frame = Frame(rps_window, padding = '3 3 12 12', width = 500)
    # allow for rows and columns and justify with specific directions
    rps_frame.grid(column = 0, row = 0, sticky = (N,W,E,S))
    # start each row and column at 0 with the same weight
    rps_frame.columnconfigure(0, weight = 1)
    rps_frame.rowconfigure(0, weight = 1)

    # designate a section of the screen for the player move list
    Label(rps_frame, text = 'Player').grid(column = 1, row = 1, sticky = W)
    Radiobutton(rps_frame, text = 'Rock', variable = player_choice, value = 1).grid(column = 1, row = 2, sticky = W)
    Radiobutton(rps_frame, text = 'Paper', variable = player_choice, value = 2).grid(column = 1, row = 3, sticky = W)
    Radiobutton(rps_frame, text = 'Scissors', variable = player_choice, value = 3).grid(column = 1, row = 4, sticky = W)

    # designate a section of the screen for the computer's move
    Label(rps_frame, text = 'Computer').grid(column = 3, row = 1, sticky = W)
    Label(rps_frame, textvariable = computer_choice).grid(column = 3, row = 3, sticky = W)

    # the play button
    Button(rps_frame, text = 'Play', command = start).grid(column = 2, row = 2)

    # player score
    Label(rps_frame, text = 'Score').grid(column = 1, row = 5, sticky = W)
    Label(rps_frame, textvariable = player_score).grid(column = 1, row = 6, sticky = W)

    # computer score
    Label(rps_frame, text = 'Score').grid(column = 3, row = 5, sticky = W)
    Label(rps_frame, textvariable = computer_score).grid(column = 3, row = 6, sticky = W)

    # game outcome
    Label(rps_frame, textvariable = result_set).grid(column = 2, row = 7)

     

if __name__ == '__main__':
    gui()
     
 

