# Question 3

import unittest
from collections import defaultdict
import bisect

'''
Given an undirected graph G, find the minimum spanning tree within G.
A minimum spanning tree connects all vertices in a graph with the smallest possible
total weight of edges. Your function should take in and return an adjacency list structured like this:
{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]}
'''

def sorted_edge_weights(graph):
    edges = set()
    for n1 in graph:
        for link in graph[n1]:
            n2 = link[0]
            weight = link[1]
            node_pair = tuple(sorted((n1, n2)))
            edges.add((weight, node_pair))
    return sorted(list(edges))

def build_new_tree(graph):
    edges = sorted_edge_weights(graph)
    new_tree = defaultdict(lambda: [])
    undirected_nodes = list(graph)
    while undirected_nodes:
       weight, (n1, n2) = edges.pop()
       if n1 in undirected_nodes:
           undirected_nodes.remove(n1)
       if n2 in undirected_nodes:
           undirected_nodes.remove(n2)
       bisect.insort(new_tree[n1], (n2, weight))
       bisect.insort(new_tree[n2], (n1, weight))

    return dict(new_tree)

def question3(graph):
    return build_new_tree(graph)

class TestQuestion3(unittest.TestCase):

    def test_graph_is_already_minimum_spanning_tree(self):
        tree = {'A': [('B', 2)],
                'B': [('A', 2), ('C', 5)],
                'C': [('B', 5)]}
        self.assertEqual(question3(tree), tree)

    def test_broad_tree(self):
        input_tree = {'A': [('B', 2)],
                      'B': [('A', 2), ('C', 5), ('D', 3)],
                      'C': [('B', 5), ('D', 1), ('E', 2)],
                      'D': [('B', 3), ('C', 1)],
                      'E': [('C', 2)]}

        output_tree = {'A': [('B', 2)],
                       'B': [('A', 2), ('D', 3)],
                       'C': [('D', 1), ('E', 2)],
                       'D': [('B', 3), ('C', 1)],
                       'E': [('C', 2)]}

        self.assertEqual(question3(input_tree),output_tree)

if __name__ == '__main__':
    unittest.main()

