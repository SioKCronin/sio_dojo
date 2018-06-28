import unittest

def fizz_buzz(n):
    for i in range(1,n+1):
        if i % 3 == 0:
            print "fizz"
        else:
            if i % 5 == 0:
                print "buzz"
            else:
                if i % 3 == 0 and i & 5 == 0:
                    print "fizzbuzz"
                else:
                    print i

fizz_buzz(15)

'''
class TestFizzBuzz(unittest.TestCase):

    def test_short_array(self):
        self.assertEqual(fizz_buzz(5), [1,2, "fizz", 4, "buzz"])

    def test_medium_array(self):
        self.assertEqual(fizz_buzz(15), [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14, "fizzbuzz"])

if __name__ == '__main__':
    unittest.main()

'''
