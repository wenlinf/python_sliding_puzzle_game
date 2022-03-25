import turtle

import utils
import config


class Buttonboard:
    """
    Class: Buttonboard
    This class represents the board displaying the buttons and the
    player moves on the game window. It can draw the buttons, display
    player moves, and draw the border of the board
    ---
    Attributes:
         board_painter(Turtle) -- the turtle instance used to draw
            the board
        border_painter(Turtle) -- the turtle instance used to draw
            the border of the button board
    """
    def __init__(self):
        """
        Method -- __init__
            The constructor of the class, creates Buttonboard
            instances
        """
        self.board_painter = turtle.Turtle()
        self.board_painter.hideturtle()
        self.border_painter = turtle.Turtle()
        self.border_painter.hideturtle()
        self.border_painter.speed(10)

    def draw_buttons(self, screen, funcs):
        """
        Method -- draw_buttons
            Draws the buttons in the button board
        Parameters:
            screen(TurtleScreen) -- the turtle screen instance where
                the game is drawn on
            funcs(list) -- a list of function names to be used as the
                onclick function callbacks of the buttons
        """
        screen.tracer(0)
        # iterate through the list of button paths in the config file
        for index, button in enumerate(config.BUTTON_PATHS):
            # draw the buttons
            button_painter = turtle.Turtle(button)
            button_painter.penup()
            button_painter.goto(config.BUTTON_X + index * 90, config.BUTTON_Y)

            # define the onclick function callback
            def on_click_button(x, y, button_name=button):
                # check the button names and bind functions to them
                if "reset" in button_name:
                    funcs["reset"]()
                if "load" in button_name:
                    funcs["load"]()
                if "quit" in button_name:
                    funcs["quit"]()
            # add onclick function to the buttons
            button_painter.onclick(on_click_button)
        screen.tracer(1)

    def display_moves(self, player_moves):
        """
        Method -- display_moves
            Displays the moves the player has made on the button board
        Parameters:
            player_moves(int) -- an integer indicating the moves the
                player has made so far
        """
        # clear the drawing if there is any
        self.board_painter.clear()

        # initialize turtle properties
        self.board_painter.penup()
        self.board_painter.pencolor("black")
        self.board_painter.setpos(config.MOVE_X, config.MOVE_Y)
        self.board_painter.pendown()

        # draw the player moves text
        player_moves_text = f"Player Moves: {player_moves}"
        self.board_painter.write(player_moves_text, align="left", font=("Arial", 18, "normal"))

    def draw_border(self):
        """
        Method -- draw_border
            Draws the border of the button board
        """
        utils.draw_board(self.border_painter,
                         config.BUTTON_BOARD_WIDTH,
                         config.BUTTON_BOARD_LENGTH,
                         config.BUTTON_BOARD_X,
                         config.BUTTON_BOARD_Y,
                         config.BUTTON_BOARD_COLOR,
                         config.BUTTON_BOARD_PENSIZE)
