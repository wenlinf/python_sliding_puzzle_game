import turtle

import utils


class Tile:
    """
    Class: Tile
    This class represents the tiles in the sliding puzzles. It
    can draw a tile and erase a tile.
    ---
    Attributes:
        tile_size(int) -- the size of the tile
        tile_image(str) -- the path to the tile image file
    """

    def __init__(self, tile_size, tile_image):
        """
        Method -- __init__
            The constructor of the class, creates tile instances
        Parameters:
            tile_size(int) -- the size of the tile
            tile_image(str) -- the path to the tile image file
        """
        # create the turtle instance to draw the tile
        self.tile_painter = turtle.Turtle()
        self.tile_painter.hideturtle()
        self.tile_size = tile_size
        self.tile_image = tile_image

    def get_tile_painter(self):
        """
        Method -- get_tile_painter
            Gets the turtle instance being used to draw the tile
        Returns the turtle instance being used to draw the tile
        """
        return self.tile_painter

    def get_tile_size(self):
        """
        Method -- get_tile_size
            Gets the size of the tile
        Returns an integer representing the size of the tile
        """
        return self.tile_size

    def set_tile_size(self, size):
        """
        Method -- set_tile_size
            Sets the size of the tile
        Parameters:
            size(int) -- the size of the tile image
        """
        self.tile_size = size

    def get_tile_image(self):
        """
        Method -- get_tile_image
            Gets the file path to image of the tile
        Returns a string representing the path to the tile image
        """
        return self.tile_image

    def set_tile_image(self, tile_image):
        """
        Method -- set_tile_image
            Sets the file path to the image of the tile
        """
        self.tile_image = tile_image

    def draw_tile(self, pos_x, pos_y):
        """
        Method -- draw_tile
            Draws the tile at the given position
        Parameters:
            pos_x: the x coordinate to start drawing
            pos_y: the y coordinate to start drawing
        """
        utils.draw_board(self.get_tile_painter(),
                         self.get_tile_size() + 2,
                         self.get_tile_size() + 2,
                         pos_x - 1,
                         pos_y + 1,
                         "black",
                         1)
        self.tile_painter.penup()
        self.tile_painter.goto(pos_x + self.get_tile_size() / 2,
                               pos_y - self.get_tile_size() / 2)
        self.tile_painter.shape(self.get_tile_image())
        self.tile_painter.showturtle()

    def erase_tile(self):
        """
        Method -- erase_tile
            Erases the tile
        """
        self.tile_painter.clear()
        self.tile_painter.hideturtle()

    def __eq__(self, other):
        """
        Method -- __eq__
            Compares the current tile instance with another one
            based on whether they have the same size and the same
            image
        Parameters:
            other(Tile) -- the other tile instance to be compared
                with the current tile instance
        Returns a boolean indicating whether the current tile
            instance equals to the other one
        """
        # check whether the two tiles have the same size and image
        return self.get_tile_image() == other.get_tile_image() and \
               self.get_tile_size() == other.get_tile_size()
