import time
import turtle


def draw_board(painter, width, length, start_x, start_y, pen_color, pen_size):
    """
    Function -- draw_board
        Draws a rectangle with the given turtle instance at the given position
        with the given length, width, pen color, and pen size.
    Parameters:
        painter(turtle) -- the turtle instance used to draw the rectangle
        width(int) -- the width of the rectangle
        length(int) -- the length of the rectangle
        start_x(int) -- the x coordinate of the starting position to draw
        start_y(int) -- the y coordinate of the starting position to draw
        pen_color(str) -- the color of the pen to draw the rectangle
        pen_size(int) -- the size of the pen to draw the rectangle
    """
    painter.penup()
    # move the turtle instance to the starting position
    painter.setpos(start_x, start_y)

    # set the pen color and size
    painter.pensize(pen_size)
    painter.pencolor(pen_color)

    # draw the rectangle
    painter.setheading(0)
    painter.pendown()
    painter.forward(width)
    painter.right(90)
    painter.forward(length)
    painter.right(90)
    painter.forward(width)
    painter.right(90)
    painter.forward(length)
    painter.penup()

def display_msg(msg_path):
    """
    Method -- display_msg
        Displays a message image based on the file path being passed in
    Parameters:
        msg_path(str) -- the file path to the image to be displayed
    """
    msg = turtle.Turtle(msg_path)
    time.sleep(3)
    msg.hideturtle()