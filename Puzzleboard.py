import random

import utils
import config


class Puzzleboard:
    """
    Class: Puzzleboard
    This class represents the puzzle board with the puzzles that users can
    play. It can draws the board border, swap tiles, and scramble the
    puzzles
    ---
    Attributes:
        moves(int) -- the moves that the user has made, default to 0
        size(int) -- the number of rows/columns of the puzzles, default to 4
        tiles(list) -- a list of Tiles representing all the tiles contained in
            the puzzle board
        board(list) -- a list of lists representing each row of tiles in the
            puzzle board
    """
    def __init__(self):
        """
        Method -- __init__
            The constructor of the class, creates Puzzleboard instances
        """
        self.moves = 0
        self.size = 4
        self.tiles = []
        self.board = []

    def get_tiles(self):
        """
        Method -- get_tiles
            Gets the list of all the tiles of the puzzle board
        Returns the list of tiles
        """
        return self.tiles

    def set_tiles(self, tiles):
        """
        Method -- set_tiles
            Sets the value of the tiles list
        Parameters:
        tiles(list) -- a list of tiles representing all the tiles in the
        puzzle board
        """
        self.tiles = tiles

    def get_board(self):
        """
        Method -- get_board
            Returns the board of the tiles of the current Puzzleboard instance
        Returns a list with nested lists representing the puzzles that the
            user is playing
        """
        return self.board

    def set_board(self, tiles):
        """
        Method -- set_board
            Sets the board of tiles of the puzzle board
        """
        # populate the list of tiles with "#"
        self.board = [["#" for _ in range(self.get_size())]
                      for _ in range(self.get_size())]

        # set the elements in the list to be the tiles
        for i in range(self.get_size()):
            for j in range(self.get_size()):
                self.board[i][j] = tiles[i * self.get_size() + j]

    def get_size(self):
        """
        Method -- get_size
            Gets the number of column/row of the puzzle board
        Returns an integer indicating the number of column/row of the board
        """
        return self.size

    def set_size(self, size):
        """
        Method -- set_size
            Sets the size of the puzzle game board
        Parameters:
            size(int) -- an integer representing the number of columns/rows
                of the puzzle game board
        """
        self.size = size

    def get_moves(self):
        """
        Method -- get_moves
            Gets the number of moves the player has made
        Returns an integer indicating how many moves the player has made
        """
        return self.moves

    def set_moves(self, moves):
        """
        Method -- set_moves
            Sets the number of moves the player has made
        Parameters:
            moves(int) -- an integer indicating how many moves the
                player has made
        """
        self.moves = moves

    def find_blank(self):
        """
        Method -- find_blank
            Finds the position of the blank tile in the puzzle game
        Returns two integers i, j indicating the position of the
            blank tile in the board list, meaning that the blank
            tile is at self.board[i][j]
        """
        # iterate through the board list and its nested lists
        for i in range(self.get_size()):
            for j in range(self.get_size()):
                # find the tile whose name has "blank"
                if "blank" in self.board[i][j].get_tile_image():
                    # return the position of the tile in the list
                    return i, j

    def find_location(self, tile):
        """
        Method -- find_location
            Finds the location of a given tile in the board list
        Parameters:
             tile(Tile) -- the tile whose position is to be found
        Returns two integers x, y indication the position of the
            given tile in the board list, which means that the
            given tile in the board list is board[x][y]
        """
        # iterate through the board list
        for x, row in enumerate(self.board):
            for y, col in enumerate(row):
                # if the given tile equals a tile in the list
                if col == tile:
                    # returns the location of the tile
                    return x, y
                    
    def is_next_to_blank(self, x, y):
        """
        Method -- is_next_to_blank
            Checks whether a given position is next to the blank tile
        Parameters:
            x(int) -- the index of the nested list the tile is in
            y(int) -- the index of the tile in its nested list
        Returns a boolean indicating whether the given position
            is next to the blank tile in the board or not
        """
        # find the blank tile in the board
        blank_x, blank_y = self.find_blank()

        # check whether the given tile is next to the blank tile
        if (abs(x - blank_x) == 1 and abs(y - blank_y) == 0)\
                or (abs(x - blank_x) == 0 and abs(y - blank_y) == 1):
            return True
        
        return False

    def swap_tile(self, tile):
        """
        Method -- swap_tile
            Swaps the tile with the blank tile if its position is
            next to the blank tile
        Parameters:
            tile(Tile) -- the tile to be swapped with the blank tile
        """
        # find the position of the blank tile
        blank_x, blank_y = self.find_blank()
        # find the position of the tile to be swapped
        tile_x, tile_y = self.find_location(tile)
        # if the tile is next to the blank tile
        if self.is_next_to_blank(tile_x, tile_y):
            # swap it with the blank tile
            self.board[blank_x][blank_y], self.board[tile_x][tile_y] = \
                self.board[tile_x][tile_y], self.board[blank_x][blank_y]
            # update the player moves
            self.moves += 1

    def scramble_board(self, player_move):
        """
        Method -- scramble_board
            Moves the blank tile in the board player_move times to scramble
            the board and makes sure the game is solvable
        Parameters:
            player_move(int) -- the maximum number of moves the player can
                make to win the game, in this function, it is the number of
                moves that the blank tile will make to scramble the board
                to ensure that the game is solvable
        """
        index = 0
        # move the blank tile player_move times to ensure the game is solvable
        while index < player_move:
            # find the position of the blank tile to move it later
            position = self.find_blank()

            # initialize the new position to move the blank tile to
            new_pos = [position[0], position[1]]

            # use a random index to decide which element in new_pos to change
            random_index = random.randint(0, 1)

            # if the blank tile is at one of the corners of the board
            # we only have two directions to move it
            if position[0] in [0, self.get_size() - 1] and \
                    position[1] in [0, self.get_size() - 1]:
                # if the element at the random index is 0, we add 1
                if position[random_index] == 0:
                    new_pos[random_index] += 1
                # if it is the size of the list - 1, we subtract 1
                elif position[random_index] == self.get_size() - 1:
                    new_pos[random_index] -= 1

            # if the blank tile is along one of the borders
            # there are three directions to move it to
            elif position[0] in [0, self.get_size() - 1] or \
                    position[1] in [0, self.get_size() - 1]:
                # if the element at the random index is already 0, add 1
                if position[random_index] == 0:
                    new_pos[random_index] += 1

                # if it is the size of the list - 1, subtract 1
                elif position[random_index] == self.get_size() - 1:
                    new_pos[random_index] -= 1
                else:
                    random_direction = random.randint(0, 1)
                    if random_direction == 0:
                        new_pos[random_index] -= 1
                    else:
                        new_pos[random_index] += 1
            # if the blank tile is not along the borders or in the corners
            else:
                # use random number to decide whether to add or subtract 1
                random_direction = random.randint(0, 1)
                # if random number is 0, subtract 1 from the element
                if random_direction == 0:
                    new_pos[random_index] -= 1
                # if random number is 1, add 1 to the element
                else:
                    new_pos[random_index] += 1

            # swap the blank tile with the tile at the new position
            self.board[position[0]][position[1]], \
                self.board[new_pos[0]][new_pos[1]] = \
                self.board[new_pos[0]][new_pos[1]], \
                self.board[position[0]][position[1]]

            # update index
            index += 1

    def draw_border(self, painter):
        """
        Method -- draw_border
            Draws the border around the puzzle board
        Parameters:
            painter(Turtle) -- the turtle instance that draws the border
        """
        # draw the border of the puzzle board
        utils.draw_board(painter,
                         config.PLAYER_BOARD_WIDTH,
                         config.PLAYER_BOARD_LENGTH,
                         config.PLAYER_BOARD_X,
                         config.PLAYER_BOARD_Y,
                         config.PLAYER_BOARD_COLOR,
                         config.PLAYER_BOARD_PENSIZE)

    def __eq__(self, other):
        """
        Method -- __eq__
            compares whether the puzzle boards are equal based on
            whether they have the same tiles in the board list
        Parameters:
            other(Puzzleboard) -- another Puzzleboard instance to be
                compared with the current instance
        Returns a boolean indicating whether the two boards are equal
        """
        # if the sizes of the two puzzles are different return False
        if self.get_size() != other.get_size():
            return False

        # iterate through the current instance and the other instance
        for i in range(self.get_size()):
            for j in range(self.get_size()):
                # compare each tile in the two lists
                if self.get_board()[i][j] != other.get_board()[i][j]:
                    return False
        return True
