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


    def is_cyclic_helper(self, v, visited, recursion_stack):
        visited[v] = True
        recursion_stack[v] = True

        for neighbor in self.graph[v]:
            if visited[neighbor] == False:
                if self.is_cyclic_helper(neighbor, visited, recursion_stack) == True:
                    return True
            elif recursion_stack[neighbor] == True:
                return True

        recursion_stack[v] = False
        return False

    def cycle_free(self):
        visited = [False] * self.V
        recursion_stack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.is_cyclic_helper(node, visited, recursion_stack) == True:
                    return False
        return True

if __name__ == '__main__':
    unittest.main()
