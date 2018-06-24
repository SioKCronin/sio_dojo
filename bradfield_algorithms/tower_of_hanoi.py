import unittest

class TestTower(unittest.TestCase):

    def test_empty_stack(self):
        data = [[], [], []]
        self.assertEqual(tower(len(data[0]), data[0], data[1], data[2]), [[], [], []]) 

    def test_one_stack(self):
        data = [[1], [], []]
        self.assertEqual(tower(len(data[0]), data[0], data[1], data[2]), [[], [1], []])

    def test_three_stack(self):
        data = [[2, 1], [], []]
        self.assertEqual(tower(len(data[0]), data[0], data[1], data[2]), [[], [2, 1], []])

def move_disk(from_pole, to_pole):
    to_pole.append(from_pole.pop())

def tower(height, from_pole, to_pole, with_pole):
    if not from_pole:
        return [from_pole, to_pole, with_pole]
    if height >= 1:
        tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        tower(height - 1, with_pole, to_pole, from_pole)
    return [from_pole, to_pole, with_pole]

if __name__ == '__main__':
    unittest.main()
