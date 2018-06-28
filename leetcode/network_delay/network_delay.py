import unittest
import collections

def networkDelayTime(times, N, K):
    graph = collections.defaultdict(list)

    for u, v, w in times:
        graph[u].append((w, v))

    print(graph)

    distances = {node: float('infinity') for node in range(1, N+1)}

    def dfs(node, elapsed):
        if elapsed >= distances[node]: return
        distances[node] = elapsed
        for time, neighbor in sorted(graph[node]):
            dfs(neighbor, time + elapsed)

    dfs(K, 0)
    ans = max(distances.values())
    return ans if ans < float('inf') else -1

class TestNetwork(unittest.TestCase):

    def test_simple(self):
        data = [[2,1,1],[2,3,1],[3,4,1]]
        self.assertEqual(networkDelayTime(data, 4, 2), 2)

if __name__ == '__main__':
    unittest.main()
