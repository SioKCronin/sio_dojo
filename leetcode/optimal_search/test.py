import random
import sys

from constants import *
from search import bfs, dfs, ucs, a_star


TEMPLATE = """
-----------------------
{algorithm}
Nodes explored: {num_explored}
Path cost: {cost}
{success}

{grid}
"""


def visualize(algorithm, grid, goal, explored):
    """
    For the given grid and search result, print a visualization
    """
    # Extract the path taken
    path = set()
    node = goal
    cost = 0
    while node in explored:
        path.add(node)
        cost += COSTS[grid[node[0]][node[1]]]
        node = explored[node]
    
    # Prepare a visual form of grid, with path overlaid
    visualization = '\n'.join(
        ' '.join(sym + ('\u0359' if (i, j) in path else '')
                 for j, sym in enumerate(row))
        for i, row in enumerate(grid))

    return TEMPLATE.format(
        algorithm=algorithm,
        num_explored=len(explored),
        cost=cost,
        success='Goal reached!' if goal in explored else 'Goal NOT reached',
        grid=visualization
    )


if __name__ == "__main__":
    """
    When running from the command line, compare every algorithm against
    one of the tests.
    """
    choice = sys.argv[1]
    if choice not in {'little', 'big', 'random'}:
        print('Usage: python3 test.py (little|big|random)')
    
    start = (0, 0)
    if choice == 'little':
        grid = [
            [S, N, N, N],
            [N, M, M, M],
            [N, R, R, R],
            [N, N, N, G]
        ]
        goal = (3, 3)
    elif choice == 'big':
        grid = [
            [S, R, R, R, M, G],
            [N, R, R, R, M, N],
            [N, M, R, R, R, N],
            [N, N, N, N, R, N],
            [N, R, N, N, N, N],
            [N, R, N, N, N, N]
        ]
        goal = (0, 5)
    elif choice == 'random':
        rows, cols = 10, 10
        goal = (random.randint(0, rows-1), random.randint(0, cols-1))
        types = (NORMAL, MOUNTAIN, RIVER)
        grid = [[random.choice(types) for _ in range(rows)] for _ in range(cols)]
        grid[start[0]][start[1]] = START
        grid[goal[0]][goal[1]] = GOAL
    
    # Run each algorithm and visualize the result
    print(visualize('BFS', grid, goal, bfs(grid, start, goal)))
    print(visualize('DFS', grid, goal, dfs(grid, start, goal)))
    print(visualize('Dijkstra’s algorithm', grid, goal, ucs(grid, start, goal)))
    print(visualize('A* search', grid, goal, a_star(grid, start, goal)))

