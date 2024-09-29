WIN_WIDTH = 800
WIN_HEIGHT = 600
TILESIZE = 20
STEPS = 1
FPS = 60

HEALTH_LAYER = 5
PLAYER_LAYER = 4
HOUSE_LAYER = 3
BLOCKS_LAYER = 2
GROUND_LAYER = 1

PLAYER_STEPS = 3

START_SCREEN = 'start_screen'
MAIN_GAME = 'main_game'

RED = (227, 145, 145)
GREEN = (145, 227, 152)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 40 characters across, G, W, I, D, S
tilemap = [
    'CCCCCCCCCCCCC1IIIIIIWWIIIIIIIIIIIIIIIIII',
    'CCCCCCCCCCCCC1IIIWWWWWWWIIIIIIIIIIIIIIII',
    'CCCCCCCCCCCCAIIIIIIIIWWWWWIIIIIIIIIIAAAA',
    'CCCCCCCCCCCAIIIIIIIIIIIWWWWWWWWIIAAACCCC',
    'CCCCCCCCCCAIIIIIIIIIIIIIIWWWIIWWACCCCCCC',
    'CCCCCCCCCAIIIIIIDDDDDDDIIIIWWIIACCCCCCCC',
    'CCCCCCCAADDDDDDDDGGGGGGDDDDWWIIACCCCCCCC',
    'CCCCCAAGGGGGGGGGGRGGGGGGGGWWWDACCCCCCCCC',
    'CCAAAGGGGGGGTGGGGGGGGBGGGGWWGG2CCCCCCCCC',
    'AAGGGBGGGGGGGGGGGGGGGGGGGWWGGG2CCCCCCCCC',
    'GGGGGGGGGGGGGGGPGGGGGGGGGGWWWWGACCCCCCCC',
    'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGWWACCCCCCCC',
    'GGGGGGGRGGGGGGGGSSSSSSGGGGGGGGGGACCCCCCC',
    'GGGGGGGGGGGGGGGSWWWWWWSGGGGTGGGGGAAACCCC',
    'GTGGGGGGGGGGGGSWWWWWWWWSGGGGGGGGGGGGAAAA',
    'GGGGGGGGGGGGGGGSWWWWWWWSGGGGGGGGGGGGGGGG',
    'GGGGGGGGGGGGGGGGSSSSSSSGGGGGGGGGGGBGGGGG',
    'GGGGGGGGGGGGGGGGGGGGGGGGGGRGGGGGGGGGGGGG',
    'GGGGGBGGGGGGGGGGGGGGGGGGGGGGGGGGGGGAAAAA',
    'GGGGGGGGGGGGRGGGGGGGGGGTGGGGGGGAAAACCCCC',
    'GGGGGGGGGGGGGGGGGGGGGGGGGGGGGAACCCCCCCCC',
    'SSSSSSGGGGGGGGGGGGGGGGGGGGGGACCCCCCCCCCC',
    'SSSSSSSSSSSSGGGGGGGGGGGGGGGACCCCCCCCCCCC',
    'WWWWWWWWWSSSSSSGTGGGGGGGGG3CCCCCCCCCCCCC',
    'WWWWWWWWWWWSSSGGGGGGGGGRGG3CCCCCCCCCCCCC',
    'WWWWWWWWWSSSSSGGGGGGGGGGGACCCCCCCCCCCCCC',
    'WWWWWWWWWWWWSSSSGGGGBGGGGACCCCCCCCCCCCCC',
    'WWWWWWWWWWWWSSSSSGGGGGGGACCCCCCCCCCCCCCC',
    'WWWWWWWWWWSSSSGGGGGGGGGGACCCCCCCCCCCCCCC',
    'WWWWWSSSSSSSSGGGGGGGGGGGACCCCCCCCCCCCCCC',

]