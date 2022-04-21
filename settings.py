import math

# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100
FPS_POSITION = (WIDTH - 65, 5)
SPEEDOMETER_POSITION = (WIDTH - 65, HEIGHT - 65)
TACHOMETER_POSITION = (WIDTH - 150, HEIGHT - 65)
TRANSMISSION_POSITION = (WIDTH - 235, HEIGHT - 65)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKY = (117, 187, 253)
ASPHALT = (96, 96, 96)

# player settings
player_pos = (700, 700)
player_angle = 0

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 900
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 2.5 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# minimap settings
MAP_SCALE = 50
TILE_SCALE = TILE // (MAP_SCALE * 1)
MAPPING_SCALE = 50

# texture settings
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# speeding settings
SPEED_DATA = [
    -2,
    0,
    20,
    27,
    35,
    40,
    47
]

SPEEDING_DATA = [
    -0.2,
    0,
    0.6,
    0.5,
    0.4,
    0.3,
    0.2
]

RPM_FACTOR = [
    1,
    1,
    1,
    0.8,
    0.6,
    0.4,
    0.2
]