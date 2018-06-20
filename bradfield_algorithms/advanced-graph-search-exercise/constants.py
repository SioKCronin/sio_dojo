START = S = 's'
GOAL = G = 'x'
NORMAL = N = ' '
MOUNTAIN = M = '^'
RIVER = R = '-'

COSTS = {
    START: 0,
    GOAL: 1,
    NORMAL: 1,
    MOUNTAIN: float('inf'),
    RIVER: 2
}

