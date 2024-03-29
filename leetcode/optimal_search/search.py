"""
Includes explored {} with the parent node path

Factor out the common aspects - the search is defined by the cost
and the heuristic. BFS and DFS can be cost driven (depths). 

Write them all out, and then try factoring out. Only go up and down.

"""
import heapq
import operator
import queue
import math

OFFSETS = [(0, 1),(-1, 0), (1, 0),(0, -1)]

def valid_pos(pos):
    if pos[0] < 4 and pos[0] >=0 and pos[1] < 4 and pos[1] >= 0:
        return True
    return False

def neighbors(grid, node):
    neighbors = []

    for  move in OFFSETS:
        new = tuple(map(operator.add, node, move))
        if valid_pos(new):
            neighbors.append(new)

    return neighbors

def euclideanDistance(point1, point2):
    return math.sqrt(
        reduce(
            (lambda memo, pair: memo + (pair[1] - pair[0]) ** 2), zip(point1, point2), 0
        )
    )

def bfs(graph, start, goal):
    if start == goal:
        return []

    frontier = queue.Queue()
    frontier.put(start)

    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        node = frontier.get()
        for neighbor in neighbors(graph, node):
            if neighbor not in came_from:
                frontier.put(neighbor)
                came_from[neighbor] = node

    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    return path.reverse()

# WIP
def dfs(graph, start, goal):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node] - visited)
    return visited

def ucs(graph, start, target):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    entry_lookup = {}
    pq = []

    for vertex, distance in distances.items():
        entry = [distance, vertex]
        # When do we check this again?
        entry_lookup[vertex] = entry
        heapq.heappush(pq, entry)

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, neighbor_distance in graph[current_vertex].items():
            distance = distances[current_vertex] + neighbor_distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                entry_lookup[neighbor][0] = distance

    # Return dict
    return distances

def a_star(graph, start, goal, euclideanDistance):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    entry_lookup = {}
    pq = []

    for vertex, distance in distances.items():
        entry = [distance, vertex]
        entry_lookup[vertex] = entry
        heapq.heappush(pq, entry)

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, neighbor_distance in graph[current_vertex].items():
            distance = distances[current_vertex] + neighbor_distance
            current_cost = euclideanDistance(neighbor)
            neighbor_cost = euclideanDistance(neighbor)
            if distance < distances[neighbor] and current_cost < neighbor_cost:
                distances[neighbor] = distance
                entry_lookup[neighbor][0] = distance
