"""
Wenlin Fang
CS 5001 Fall 2021
Final Project

This program runs a slider puzzle game. Player needs to input
their names and the maximum number of games they want to make
to start the game. While playing the game, players can choose
to reset the game, load a new game, or quit the game. If users
finish the puzzles within the maximum number of moves, they win
the game and their name and score will be written into the
leaderboard file for display. Users can also see how many moves
they have already made on the game window.
"""
import logging
import os
import turtle

import config
import utils
from PuzzleGame import PuzzleGame


def play_game():
    """
    Function - play_game
        Configures the resources that will be used during the game,
        including configuring the error logging, creating the
        turtle instance to draw the game, and the turtle screen
        instance where the game will be drawn, registering the
        images that will be used by the game to the screen, checking
        the leaderboard file. Then starts the game
    """
    # configure the log file path and logging format
    logging.basicConfig(filename=config.ERROR_LOG,
                        format=config.LOG_FORMAT)

    # create　a screen instance and set up screen size
    screen = turtle.Screen()
    screen.setup(config.SCREEN_WIDTH, config.SCREEN_LENGTH)

    # create a turtle instance
    painter = turtle.Turtle()
    painter.speed(10)
    painter.hideturtle()

    # load all the images in Resources and add to screen
    resources = load_resources()
    for resource in resources:
        screen.addshape(resource)

    # check whether leaderboard file exists
    check_leader_board()

    # create a puzzle game instance and start game
    puzzle_game = PuzzleGame(painter, screen)
    puzzle_game.start_game()


def check_leader_board():
    """
    Function -- check_leader_board
        Checks whether the leaderboard file exists. If not, logs
        the error and displays an error message to the user and
        creates a leaderboard file
    """
    # if the file doesn't exist
    if not os.path.exists(config.LEADER_BOARD_PATH):
        # display an error to the user and log the error
        utils.display_msg(config.LEADERBOARD_ERR)
        logging.error("Leader file doesn't exist. Creating one.")

        # create a leaderboard file at the configured path
        leader_file = open(config.LEADER_BOARD_PATH, "w")
        leader_file.close()


def load_resources():
    """
    Function -- load_resources
        Loads all the images in the Resources directory
    Returns a list of strings which are the paths to all the
        images in the Resources folder
    """
    # create a list to store all the image paths
    resources = []

    # get all the files under the Resources folder
    path = "Resources/"
    files = os.listdir(path)

    # iterate through the files and add to the list
    for file in files:
        resources.append(path + file)

    return resources


def main():
    """
    Program entry point
    """
    play_game()


if __name__ == "__main__":
    main()
