'''
KNIGHTS DIAL
Imagine you place a knight chess piece on a phone dial pad. This chess piece moves 
in an uppercase “L” shape: two steps horizontally followed by one vertically, or 
one step horizontally then two vertically.

Suppose you dial keys on the keypad using only hops a knight can make. 
Every time the knight lands on a key, we dial that key and make another hop. 
The starting position counts as being dialed.

How many distinct numbers can you dial in N hops from a particular starting position?
'''

import unittest

class TestKnightsDial(unittest.TestCase):

    def test_1(self):
        self.assertEqual(knights_dial1(1, 3), 8)
        self.assertEqual(knights_dial1(1, 0), 1)

    def test_2(self):
        self.assertEqual(knights_dial2(1, 3), 8)

    def test_3(self):
        self.assertEqual(knights_dial3(1, 3), 8)

dial_map = {1: [8, 6], 
            2: [7, 9], 
            3: [4, 8], 
            4: [3, 9], 
            5: [],
            6: [1, 7],
            7: [2, 6], 
            8: [1, 3], 
            9: [2, 4], 
            0: [4, 6]
           }


def knights_dial3(start, n):
    memo = {}

    def helper(position, n):
        if (position, n) in memo:
            return memo[(position, n)]
 
        if n == 0: return 1

        else:
            num_sequences = 0
            for valid in dial_map[position]:
                num_sequences += helper(valid, n-1)
            memo[(position, n)] = num_sequences
            return num_sequences

    return helper(start, n)

def knights_dial2(start, n):
    if n == 0: return 1
    if n == 1:
        return len(dial_map[start])
    n -= 1
    return sum([knights_dial2(child, n) for child in dial_map[start]])  

def knights_dial1(start, n):
    if n <= 0: return 1

    queue = [start]
    while n > 0:
        new_queue = []
        while queue:
            node = queue.pop(0)
            new_queue.extend(dial_map[node])
        n -= 1
        queue = new_queue

    return len(new_queue)

if __name__ == '__main__':
    unittest.main()
