import os
import logging
import turtle
import time

from Buttonboard import Buttonboard
from Leaderboard import Leaderboard
from Puzzleboard import Puzzleboard
from Tile import Tile
import config
import utils


class PuzzleGame:
    """
    Class: PuzzleGame
    This class represents the sliding puzzle game that users will be playing.
    It can start the game, load a new game, reset the game, quit the game,
    display game results
    ---
    Attributes:
        painter(Turtle) -- the turtle instance that will draw the game
        screen(TurtleScreen) -- the graphics window that the game will be
            drawn on
        game(str) -- the path to the game file that is currently being played
        move(int) -- the maximum moves user can make to win the game (default
             is 0)
        player_name(str) -- the name of the current player
        puzzle_board(Puzzleboard) -- the puzzle board that has all the tiles
        origin_board(Puzzleboard) -- the puzzle board in an unscrambled state
        leader_board(Leaderboard) -- the leaderboard on the game window
        button_board(Buttonboard) -- the board displaying the buttons and
            player moves
    """
    def __init__(self, painter, screen):
        """
        Method -- __init__
            The constructor of the class PuzzleGame, creates PuzzleGame
            instances
        Parameters:
            painter(Turtle) -- the turtle instance that draws the graphics
                of the game
            screen(TurtleScreen) -- the turtle screen instance that the
                game is drawn on
        """
        self.painter = painter
        self.screen = screen
        self.game = ""
        self.move = 0
        self.player_name = ""
        self.puzzle_board = Puzzleboard()
        self.origin_board = Puzzleboard()
        self.leader_board = Leaderboard(painter)
        self.button_board = Buttonboard()

    def set_leader_board(self, leader_board):
        """
        Method -- set_leader_board
            Sets the value of the leaderboard
        Parameters:
            leader_board(Leaderboard) -- the Leaderboard instance
                representing the leader board section in the game window
        """
        self.leader_board = leader_board

    def get_leader_board(self):
        """
        Method -- get_leader_board
            Returns the value of the leaderboard
        Returns the leaderboard instance that represents the leaderboard
            section
        """
        return self.leader_board

    def set_move(self, move):
        """
        Method -- set_move
            Sets the value of the maximum moves user can make to win the game
        Parameters:
             move(int) -- the maximum number of moves user can make to win
                 the game
        """
        self.move = move

    def get_move(self):
        """
        Method -- get_move
            Returns the number of the moves user can make to win the game
        Returns an integer representing the maximum moves user can make to
            win the game
        """
        return self.move

    def set_player_name(self, player_name):
        """
        Method -- set_player_name
            Sets the name of the player
        Parameters:
            player_name(str) -- the name of the current player
        """
        self.player_name = player_name

    def get_player_name(self):
        """
        Method -- get_player_name
            Returns the name of the current player
        Returns a string representing the name of the current player
        """
        return self.player_name

    def set_puzzle_board(self, puzzle_board):
        """
        Method -- set_puzzle_board
            Sets the current puzzle board
        Parameters:
            puzzle_board(Puzzleboard) -- the new puzzle board instance
                that will be displayed in the game window
        """
        self.puzzle_board = puzzle_board

    def get_puzzle_board(self):
        """
        Method -- get_puzzle_board
            Returns the current puzzle board instance of the puzzle game
        Returns a Puzzleboard instance representing the current puzzle board
        """
        return self.puzzle_board

    def set_game(self, game):
        """
        Method -- set_game
            Sets the path of the game currently being played
        Parameters:
            game(str) -- a string representing the name of the .puz file
                containing the information of the current game
        """
        self.game = game

    def get_game(self):
        """
        Method -- get_game
            Returns the name of the .puz file of the current game
        Returns a string representing the name of the .puz file
                containing the information of the current game
        """
        return self.game

    def splash_screen(self):
        """
        Method -- splash_screen
            Displays the splash screen at the beginning of the game
        """
        # create a turtle instance to display the splash screen image
        splash = turtle.Turtle(config.SPLASH_PIC_PATH)
        # hide the splash screen after 3 seconds
        time.sleep(3)
        splash.hideturtle()

    def prompt_user(self):
        """
        Method -- prompt_user
            Asks for user name and the maximum moves they want to make to win
            the game, then updates the move and the player_move attributes of
            the PuzzleGame instance
        """
        # prompt for user inputs
        player_name = self.screen.textinput("name", "What's your name?")
        move = int(self.screen.numinput("move",
                                        "Enter the number of moves you "
                                        "want(5-200)",
                                        minval=5,
                                        maxval=200))

        # update the player_name and the move attributes based on user inputs
        self.set_player_name(player_name)
        self.set_move(move)

    def load_all_games(self):
        """
        Method -- load_all_games
            Loads all the .puz files in the current directory. If
            no .puz file is found, the game will end because there
            is no puzzle to play
        Returns a list of strings with the names of all the .puz files
        """
        # load all the .puz files from the current directory
        games = []
        game_files = os.listdir()
        for game_file in game_files:
            if game_file.endswith(".puz"):
                games.append(game_file)

        # set the default game to be the first one in the game list
        if len(games) != 0:
            self.set_game(games[0])
            return games
        else:
            # if no puz file is found display error and end game
            utils.display_msg(config.FILE_ERR)
            logging.error(f"No puz file found.")
            self.game_credit()
            quit()

    def load_meta_data(self, game_path):
        """
        Method -- load_meta_data
            Loads the information of the games from their .puz file.
        Parameters:
            game_path(str) -- a string representing the path of the
                .puz file of the game
        Returns a string, an integer, and a list of strings representing
            the name of the current game thumbnail, the size of the
            tiles, and a list of strings containing all the puzzle tile
            image names
        """
        # create a dictionary to store the data in .puz file
        data_dict = {}
        with open(game_path) as infile:
            for line in infile:
                meta_data, data = line.strip().split(":")
                data_dict[meta_data] = data.strip()

        # get the name of the thumbnail image and add to screen
        thumbnail = data_dict["thumbnail"]
        if not os.path.isfile(thumbnail):
            logging.error("Thumbnail image doesn't exist.")
            return
        self.screen.addshape(thumbnail)

        # get the tile size from the meta data
        tile_size = int(data_dict["size"])

        # create a list to store the names of all puzzle images
        puzzle_images = []
        for key in data_dict.keys():
            # if the key is a number, store its value
            if key.isdecimal():
                puzzle_images.append(data_dict[key])
                if not os.path.isfile(data_dict[key]):
                    logging.error("Tile image doesn't exist.")
                    return
                self.screen.addshape(data_dict[key])

        # if the number of puzzle images is not in 4, 9, 16, log error
        if len(puzzle_images) not in [4, 9, 16]:
            logging.error(f"Only {len(puzzle_images)} tiles found. Not a valid puzzle.")
            return
        return thumbnail, tile_size, puzzle_images

    def redraw_game(self):
        """
        Method -- redraw_game
            Redraws the thumbnail, puzzle board, and player move section when
            a new game is loaded
        """
        # erase the original game information
        self.erase_game()

        # create and draw a new puzzle board with the newly loaded puzzles
        self.initialize_board()
        self.draw_puzzle_board()

        # draw the new thumbnail at the leaderboard
        self.leader_board.draw_thumbnail()

        # update the player move section
        self.button_board.display_moves(self.puzzle_board.get_moves())

    def initialize_board(self):
        """
        Method -- initialize_board
            Loads the thumbnail, tile size, puzzle images to be used in the
            game. Sets the attributes of the leaderboard, and the puzzle
            board with the loaded thumbnail, tile size and puzzle images
        """
        # if the data are not loaded successfully
        if not self.load_meta_data(self.get_game()):
            # display error message and stop processing
            msg = turtle.Turtle(config.FILE_ERR)
            self.screen.update()
            time.sleep(3)
            msg.hideturtle()
            return

        # load the thumbnail, tile size, and puzzle images of the game
        thumbnail, tile_size, puzzle_images = \
            self.load_meta_data(self.get_game())

        # create the tiles based on the size and the loaded puzzle images
        tiles = []
        self.screen.tracer(0)
        for puzzle_image in puzzle_images:
            tiles.append(Tile(tile_size, puzzle_image))
        self.screen.tracer(1)

        # set the size, tiles, board attributes of the puzzle board
        self.puzzle_board.set_size(int(len(puzzle_images) ** 0.5))
        self.puzzle_board.set_tiles(tiles)
        self.puzzle_board.set_board(tiles)

        # set the same size, tiles, board attributes for the original board
        self.origin_board.set_size(int(len(puzzle_images) ** 0.5))
        self.origin_board.set_tiles(tiles)
        self.origin_board.set_board(tiles)

        # scramble the puzzle board
        self.puzzle_board.scramble_board(self.get_move())

        # set the thumbnail_img attribute of the leaderboard
        self.get_leader_board().set_thumbnail_img(thumbnail)

    def start_game(self):
        """
        Method -- start_game
            Starts the puzzle game, displays the splash screen, loads all
            the available games, prompts for user inputs, creates the
            components in the puzzle board, leaderboard, and the button
            board
        """
        # display the splash screen
        self.splash_screen()

        # load all the games
        self.load_all_games()

        # hide the turtle
        self.painter.hideturtle()

        # ask for user input
        self.prompt_user()

        # create and draw the puzzle board
        self.initialize_board()
        self.puzzle_board.draw_border(self.painter)
        self.draw_puzzle_board()

        # display the components of the leaderboard
        self.get_leader_board().draw_leaderboard()

        # display the components of the button board
        self.button_board.draw_border()
        funcs = {"reset": self.reset_game,
                 "load": self.load_new_game,
                 "quit": self.quit_game}
        self.button_board.draw_buttons(self.screen, funcs)
        self.button_board.display_moves(self.puzzle_board.get_moves())

    def reset_game(self):
        """
        Method -- reset_game
            Resets the puzzles to their unscrambled state
        """
        # iterate over the items in the original board
        for x, row in enumerate(self.origin_board.get_board()):
            for y, col in enumerate(row):
                # use the original board to update the current puzzle board
                self.puzzle_board.get_board()[x][y] = \
                    self.origin_board.get_board()[x][y]

        # draw the updated puzzle board
        self.draw_puzzle_board()

    def load_new_game(self):
        """
        Method - load_new_game
            Loads a new puzzle game
        """
        # load all the games
        games = self.load_all_games()

        # ask the user to choose the new game to load
        games_text = ""
        for game in games:
            games_text += game + "\n"
        prompt = "Enter the name of the puzzle you wish to load. Choices " \
                 "are:\n" + games_text
        new_game = self.screen.textinput("game", prompt)

        # if user choose an invalid game, display error message
        if new_game not in games:
            utils.display_msg(config.FILE_ERR)
            logging.error(f"{new_game} is not a valid game.")
        else:
            self.screen.tracer(0)
            # set the game attribute to be the newly loaded game
            self.set_game(new_game)
            # redraw the puzzle game
            self.redraw_game()
            self.screen.tracer(1)

    def erase_game(self):
        """
        Method -- erase_game
            Erases the old thumbnail and the tiles, sets the player moves to 0
        """
        # erase the thumbnail
        self.get_leader_board().erase_thumbnail()

        # sets the player move to 0
        self.get_puzzle_board().set_moves(0)

        # erase all the tiles
        tiles = self.get_puzzle_board().get_tiles()
        for tile in tiles:
            tile.erase_tile()

    def display_result(self, result):
        """
        Method -- display_result
            Displays messages based on the game result that is passed in.
            If user wins the game, display the winner message, otherwise,
            displays the lose message. Ends the game after displaying the
            messages
        Parameters:
            result(str) -- a string that is either "lose" or "win" to
                indicate the result of the game in order to display the
                corresponding message to the user
        """
        # if user loses the game, display the lose game message
        if result == "lose":
            utils.display_msg(config.LOSE_GAME)

        # if user wins the game, display the win game message
        elif result == "win":
            self.get_leader_board().add_to_leaderboard(
                self.get_puzzle_board().get_moves(),
                self.get_player_name())
            utils.display_msg(config.WIN_GAME)

        # show the game credit image and end game
        self.game_credit()

    def quit_game(self):
        """
        Method -- quit_game
            Quits the game and displays the quit game image to user
        """
        utils.display_msg(config.QUIT_GAME)
        self.game_credit()

    def game_credit(self):
        """
        Method -- game_credit
            Displays the credit image every time when the game ends,
            then ends the game
        """
        # display the credit image
        utils.display_msg(config.GAME_CREDIT)

        # quit the turtle graphics
        turtle.bye()

        # end the program
        quit()

    def draw_puzzle_board(self):
        """
        Method -- draw_puzzle_board
            Draws the tiles in the puzzle board
        """
        self.screen.tracer(0)

        # iterate through the puzzle board list
        for x in range(self.puzzle_board.get_size()):
            for y in range(self.puzzle_board.get_size()):
                # get the turtle instance and tile size of each tile
                tile = self.puzzle_board.get_board()[x][y]
                tile_painter = tile.get_tile_painter()
                tile_painter.penup()
                tile_size = tile.get_tile_size()

                # set position to make the puzzle game align from the center
                start_x = config.PLAYER_BOARD_X + \
                          config.PLAYER_BOARD_WIDTH / 2 - \
                          self.puzzle_board.get_size() * tile_size / 2 + \
                          y * (tile_size + 2)
                start_y = config.PLAYER_BOARD_Y - \
                          config.PLAYER_BOARD_LENGTH / 2 + \
                          self.puzzle_board.get_size() * tile_size / 2 - \
                          x * (tile_size + 2)
                # draw each tile at the calculated positions
                tile.draw_tile(start_x, start_y)

                # define callback function of the onclick events of the tiles
                def swap(x, y, tile=tile):
                    # swap the tile if it is next to the blank tile
                    self.puzzle_board.swap_tile(tile)

                    # display the moves the user has made
                    self.button_board.display_moves(self.puzzle_board.get_moves())

                    # update the puzzle board after the swap
                    self.draw_puzzle_board()

                    # if user made more moves than the maximum, they lose
                    if self.puzzle_board.get_moves() >= self.move and \
                            self.puzzle_board != self.origin_board:
                        self.display_result("lose")

                    # if user finishes the puzzle within the maximum, they win
                    elif self.puzzle_board.get_moves() <= self.move and \
                            self.puzzle_board == self.origin_board:
                        self.display_result("win")
                # define an onclick function for each tile for tile swapping
                tile_painter.onclick(swap)
        self.screen.tracer(1)
