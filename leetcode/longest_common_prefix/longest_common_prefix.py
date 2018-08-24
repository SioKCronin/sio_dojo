import unittest

class TestLongestCommonPrefix(unittest.TestCase): 

    def test_leet_example_1(self):
        self.assertEqual(longest_common_prefix(['flower', 'flow', 'flight']), 'fl')

    def test_leet_example_1(self):
        self.assertEqual(longest_common_prefix(['dog', 'racecar', 'car']), '')

    def test_leet_example_1(self):
        self.assertEqual(longest_common_prefix(['flowerish', 'flower', 'flow']), 'flow')

def longest_common_prefix(words):
    prefix = ''
    count = 0
    leader = min(words, key=len)

    while count < len(leader): 
        for word in words[1:]:
            if word[count] != leader[count]:
                return prefix
        prefix += leader[count]
        count += 1
    return prefix

if __name__ == '__main__':
    unittest.main()
