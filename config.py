# screen size
SCREEN_WIDTH = 800
SCREEN_LENGTH = 800

# leader board positions
LEADER_BOARD_X = 110
LEADER_BOARD_Y = 300
LEADER_BOARD_WIDTH = 240
LEADER_BOARD_LENGTH = 460
LEADER_BOARD_COLOR = "blue"
LEADER_BOARD_PENSIZE = 5

# leader display properties
LEADER_X = 118
LEADER_Y = 200
LEADER_PENSIZE = 8

# thumbnail image positions
THUMBNAIL_X = LEADER_BOARD_X + 165
THUMBNAIL_Y = LEADER_BOARD_Y - 30

# puzzle board positions
PLAYER_BOARD_X = -370
PLAYER_BOARD_Y = 300

PLAYER_BOARD_WIDTH = 460
PLAYER_BOARD_LENGTH = 460
PLAYER_BOARD_COLOR = "black"
PLAYER_BOARD_PENSIZE = 5

# button board positions
BUTTON_BOARD_X = -370
BUTTON_BOARD_Y = -180
BUTTON_BOARD_WIDTH = 720
BUTTON_BOARD_LENGTH = 100
BUTTON_BOARD_COLOR = "black"
BUTTON_BOARD_PENSIZE = 5

# button position
BUTTON_X = 80
BUTTON_Y = -230

# player move position
MOVE_X = -330
MOVE_Y = -240

# file paths
LEADER_BOARD_PATH = "leaderboard.txt"
LEADERBOARD_ERR = "Resources/leaderboard_error.gif"
SPLASH_PIC_PATH = "Resources/splash_screen.gif"
FILE_ERR = "Resources/file_error.gif"
LOSE_GAME = "Resources/Lose.gif"
WIN_GAME = "Resources/winner.gif"
QUIT_GAME = "Resources/quitmsg.gif"
GAME_CREDIT = "Resources/credits.gif"
BUTTON_PATHS = ["Resources/resetbutton.gif", "Resources/loadbutton.gif", "Resources/quitbutton.gif"]

# error logging
ERROR_LOG = "5001_puzzle.err"
LOG_FORMAT = "TIMESTAMP: %(asctime)s - ERROR: %(message)s - LOCATION: %(module)s.%(funcName)s"
