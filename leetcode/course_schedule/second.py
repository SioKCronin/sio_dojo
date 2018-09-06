import unittest

class TestCourseSchedule(unittest.TestCase):

    def test_leet_examples(self):
        g = Graph(2, [[1, 0]])
        self.assertTrue(g.cycle_free())

    def test_leet_example2(self):
        g = Graph(2, [[1,0], [0,1]])
        self.assertFalse(g.cycle_free()) 

def create_graph(prereqs):
    graph = {}
    for pair in prereqs:
        if pair[1] in graph:
            graph[pair[1]].append(pair[0])
        else:
            graph[pair[0]] = [pair[1]]
    return graph


class Graph():

    def __init__(self, N, prereqs):
        self.graph = create_graph(prereqs)
        self.V = N

    def add_edge(self, u, v):
        self.graph[u].append(v)

    
