from constants import MOUNTAIN, COSTS
from structures import Queue, Stack, PriorityQueue


_DELTAS = ((-1, 0), (0, -1), (1, 0), (0, 1))


def _successors(grid, location):
    """
    Return the set of co-ordinates that can be reached from the given location
    """
    i, j = location
    return {(i+di, j+dj) for di, dj in _DELTAS
            if 0 <= i+di < len(grid) and 0 <= j+dj < len(grid[0])
            and grid[i+di][j+dj] != MOUNTAIN}


def _search(queue, g, h):
    """
    A generic search function, which can be used to construct
    BFS, DFS, UCS or A* based on the given "queue" and heuristic function.
    """
    def inner(grid, start, goal):
        frontier = queue
        frontier.add((0, 0, start, None))
        explored = {}
        
        while not frontier.empty():
            _, cost, node, parent = frontier.pop()

            if node in explored:
                continue

            explored[node] = parent

            if node == goal:
                return explored
            
            neighbors = _successors(grid, node)
            for neighbor in neighbors:
                if neighbor not in explored:
                    step_cost = g(grid, goal, neighbor)
                    future_cost = h(grid, goal, neighbor)
                    frontier.add((cost + step_cost + future_cost,
                                  cost + step_cost,
                                  neighbor,
                                  node))

        return explored

    return inner


def one(*args):
    return 1


def zero(*args):
    return 0


def cost(grid, _, node):
    """Determine cost of traversing given node"""
    i, j = node
    return COSTS[grid[i][j]]


def manhattan(_, goal, node):
    """Manhattan distance from node to goal, for heuristic"""
    i, j = node
    gi, gj = goal
    return abs(gi - i) + abs(gj - j)


bfs = _search(Queue(), one, zero)
dfs = _search(Stack(), one, zero)
ucs = _search(PriorityQueue(), cost, zero)
a_star = _search(PriorityQueue(), cost, manhattan) 

