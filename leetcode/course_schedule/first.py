import unittest
import collections

class TestCanFinish(unittest.TestCase):

    def test_leet_example(self):
        self.assertTrue(canFinish(2, [[0,1]]))
        self.assertFalse(canFinish(2, [[0,1], [1,0]]))

def can_finish(numCourses, prerequisites):

    # Guard clause
    if not prerequisites:
        return True

    # Build the graph
    graph = collections.defaultdict(list)
    for course, pre_course in prerequisites:
        graph[pre_course].append(course)
    seen, in_stack = set(), set()

    # Define cycle
    def cycle(seen, in_stack, v):
        seen.add(v)
        in_stack.add(v)
        for neighbor in graph[v]:
            if neighbor not in seen:
                if cycle(seen, in_stack, neighbor):
                    return True
            else:
                if neighbor in in_stack:
                    return True
        in_stack.discard(v)
        return False

    # Check all prereqs
    for i, j in prerequisites:
        if j not in seen:
            if cycle(seen, in_stack, j):
                return False
    return len(seen) <= numCourses

if __name__ == '__main__':
    unittest.main()
