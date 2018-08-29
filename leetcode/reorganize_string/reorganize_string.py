import unittest
from collections import Counter

class TestReorganizeString(unittest.TestCase):

    def test_leet_examples(self):
        self.assertEqual("aba", reorganize_string("aab"))
        self.assertEqual("", reorganize_string("aaab"))

    def test_my_examples(self):
        self.assertEqual("ababa", reorganize_string("aaabb"))
        self.assertEqual("abab", reorganize_string("aabb"))
        self.assertEqual("abcab", reorganize_string("caabb"))

def reorganize_string(s):
    output = ""
    chars = list(s)
    i = 0
    while i < len(s):
        most_common = Counter(chars).most_common(2)
        if len(output) == 0:
            output += most_common[0][0]
            chars.remove(most_common[0][0])
            i += 1

        if len(most_common) == 2:
            if output[-1] == most_common[0][0]:
                output += most_common[1][0]
                chars.remove(most_common[1][0])
                i += 1
            else:
                output += most_common[0][0]
                chars.remove(most_common[0][0])
                i += 1
        else:
            if output[-1] == most_common[0][0]:
                return ""
            else:
                output += most_common[0][0]
                chars.remove(most_common[0][0])
                i += 1
    return output

if __name__ == '__main__':
    unittest.main()
