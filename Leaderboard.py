import os
import turtle

import config
import utils


class Leaderboard:
    """
    Class: Leaderboard
    This class represents the leaderboard in the sliding puzzle game window.
    It draws the leaderboard, adds new winners to the leaderboard, displays
    the leaders on the leaderboard, as well as draws and erases the thumbnail
    ---
    Attributes:
        painter(Turtle) -- the turtle instance that draws the board
        thumbnail_img(str) -- the file path of the thumbnail image
        thumbnail_painter(Turtle) -- the turtle instance that draws
            the thumbnail
    """
    def __init__(self, painter):
        """
        Method -- __init__
            The constructor of the class, creates Leaderboard instances
        Parameters:
            painter(Turtle) -- the turtle instance that draws the leaderboard
        """
        self.painter = painter
        self.thumbnail_img = ""
        self.thumbnail_painter = turtle.Turtle()
        self.thumbnail_painter.hideturtle()

    def set_thumbnail_img(self, thumbnail_img):
        """
        Method -- set_thumbnail_img
            Sets the file path of the thumbnail image in the leaderboard
        Parameters:
            thumbnail_img(str) -- the file path of the thumbnail image
        """
        self.thumbnail_img = thumbnail_img

    def get_thumbnail_img(self):
        """
        Method -- get_thumbnail_img
            Gets the current thumbnail image file path
        Returns a string representing the file path to the thumbnail image
        """
        return self.thumbnail_img

    def set_thumbnail_painter(self, thumbnail_painter):
        """
        Method -- set_thumbnail_painter
            Sets the turtle instance to be used to draw the thumbnail
        Parameters:
            thumbnail_painter(Turtle) -- the turtle instance to be
                used to draw the thumbnail
        """
        self.thumbnail_painter = thumbnail_painter

    def get_thumbnail_painter(self):
        """
        Method -- get_thumbnail_painter
            Gets the turtle instance being used to draw the thumbnail
        Returns the turtle instance being used to draw the thumbnail
        """
        return self.thumbnail_painter

    def draw_leaderboard(self):
        """
        Method -- draw_leaderboard
            Draws the leaderboard border, loads the leaders and displays them,
            and draws the thumbnail
        """
        # draw the border of the leaderboard
        utils.draw_board(self.painter,
                         config.LEADER_BOARD_WIDTH,
                         config.LEADER_BOARD_LENGTH,
                         config.LEADER_BOARD_X,
                         config.LEADER_BOARD_Y,
                         "blue",
                         5)
        self.painter.penup()

        # display the leaders on the leaderboard
        self.painter.setpos(config.LEADER_BOARD_X + 10,
                            config.LEADER_BOARD_Y - 40)
        self.painter.write("Leaders:",
                           align="left",
                           font=("Arial", 18, "normal"))
        self.load_leaders()

        # draw the thumbnail
        self.draw_thumbnail()

    def load_leaders(self):
        """
        Method -- load_leaders
            Loads the leaders from the leaderboard file and displays the
            first 5 records on the screen
        """
        # read the file with leaderboard records
        with open(config.LEADER_BOARD_PATH, "r") as src_file:
            # iterate through the lines in the file
            for index, line in enumerate(src_file):
                # only read the first five records
                if index < 5:
                    self.painter.setpos(config.LEADER_X,
                                        config.LEADER_Y - index * 23)
                    self.painter.pencolor(config.LEADER_BOARD_COLOR)
                    self.painter.pensize(config.LEADER_PENSIZE)

                    # write the record to the screen
                    self.painter.write(line,
                                       align="left",
                                       font=("Arial", 16, "normal"))

    def add_to_leaderboard(self, moves, player_name):
        """
        Method -- add_to_leaderboard
            Adds the current player and their score to the leaderboard
            file if they win the game
        Parameters:
            moves(int) -- the number of moves the player has made
            player_name(str) -- the name of the player
        """
        # create lists to store leaders and their scores read from the file
        leaders = []
        scores = []

        # read the leaderboard file
        new_content = ""
        with open(config.LEADER_BOARD_PATH, "r") as src_file:
            # if the leaderboard file is empty
            if os.path.getsize(config.LEADER_BOARD_PATH) == 0:
                # only add the new leader and their score
                new_content += f"{str(moves)}:{player_name}\n"
            # if the file is not empty
            else:
                # iterate through each line in the file
                for line in src_file:
                    # if the line is not empty
                    if line.strip() != "":
                        # split the line and save the score and the name
                        score, name = line.strip().split(":")
                        # add the name and score to the lists
                        leaders.append([int(score.strip()), name.strip()])
                        scores.append(int(score.strip()))

                # find the position where the new leader should be inserted
                insert_index = self.find_insert_pos(scores, moves)

                # create a variable to check whether new record has been added
                inserted = False
                # iterate through the list of leaders
                for index in range(len(leaders) + 1):
                    # insert the new leader when reaching the insertion index
                    if index == insert_index:
                        new_content += f"{str(moves)} : {player_name}\n"
                        # set inserted to True
                        inserted = True
                    # when new record hasn't been inserted
                    elif not inserted:
                        # get leaders from the list at the current index
                        new_content += f"{str(leaders[index][0])} : " \
                                       f"{leaders[index][1]}\n"
                    # when new record has been added already
                    else:
                        # get leaders from the list at current index - 1
                        new_content += f"{str(leaders[index - 1][0])} : " \
                                       f"{leaders[index - 1][1]}\n"
            # write the updated leaderboard content to the file
            with open(config.LEADER_BOARD_PATH, "w") as outfile:
                outfile.write(new_content)

    def find_insert_pos(self, scores, new_score):
        """
        Method -- find_insert_pos
            Finds the position where the new leader should be inserted
            in the leaderboard file
        Parameters:
            scores(list) -- a sorted list of integers of all the current
                scores in the leaderboard file
            new_score(int) -- the score of the current player
        Returns an integer representing the index in the list where the
            new score should be inserted
        """
        # iterate over the list of scores
        for index, score in enumerate(scores):
            # if new score is less than the first score
            if index == 0 and new_score < score:
                # the new score should be inserted at index 0
                return index
            # if new score equals to the current score
            if score == new_score:
                # the new score should take the place of the current score
                return index
            if index <= len(scores) - 2:
                # if the new score is between current score and its next one
                if score < new_score < scores[index + 1]:
                    # new score should be inserted after current score
                    return index + 1
            # if new score is greater than the last score
            else:
                # should insert it at the end of the list
                return len(scores)

    def draw_thumbnail(self):
        """
        Method -- draw_thumbnail
            Draws the thumbnail at the leaderboard
        """
        self.thumbnail_painter.penup()
        self.thumbnail_painter.goto(config.THUMBNAIL_X, config.THUMBNAIL_Y)
        self.thumbnail_painter.showturtle()
        self.thumbnail_painter.shape(self.thumbnail_img)

    def erase_thumbnail(self):
        """
        Method -- erase_thumbnail
            Erases the thumbnail from the window
        """
        self.thumbnail_painter.hideturtle()

