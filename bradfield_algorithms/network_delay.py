import unittest
import heapq


def build_graph(times, N):
    graph = {}

    for entry in times:
        if entry[0] in graph:
            graph[entry[0]][entry[1]] = entry[2]
        else:
            graph[entry[0]] = {}
            graph[entry[0]][entry[1]] = entry[2]

    return graph


def networkDelayTime(times, N, K):
    """
    times: List[List[int]]
       travel times as directed edges 'times[i] = (u, v, w), where 'u' is the
       source, 'v' is the target, and 'w' is the time it takes for a signal
       to travel from source to target. 
    N: int
       number of network nodes
    K: int
       start node
    rtype: int
    """

    graph = build_graph(times, N)

    distances = {vertex: float('infinity') for vertex in graph}
    # We keep track of edges, but start with a node?
    distances[(K, 0)] = 0

    tracker = set([i for i in range(N)])
    entry_lookup = {}
    pq = []

    for vertex, length in graph.items():
        entry = [length, vertex]
        entry_lookup[vertex] = entry
        heapq.heappush(pq, entry)

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, neighbor_length in graph[current_vertex].items():
            distance = distances[current_vertex] + neighbor_length
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                entry_lookup[neighbor][0] = distance

    # We need some guard clause for checking that all Nodes were reached

    return sum(distances.items())

class TestNetwork(unittest.TestCase):

    def test_simple(self):
        data = [[2,1,1],[2,3,1],[3,4,1]]
        self.assertEqual(networkDelayTime(data, 4, 2), 2)

if __name__ == '__main__':
    unittest.main()
