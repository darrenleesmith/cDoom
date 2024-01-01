import math

# game settings

# the below settings set the window size and frame rate
RES = WIDTH, HEIGHT = 1600, 900 # resolution
FPS = 60 # game frames per second

# Player settings:

PLAYER_POS = 1.5, 5 # mini map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

# Ray Casting settings;

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20