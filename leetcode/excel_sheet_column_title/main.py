import unittest

class TestExcelSheetColumnTitle(unittest.TestCase):

    def test_single(self):
        self.assertEqual(titler(1), 'A')
        self.assertEqual(titler(2), 'B')
        self.assertEqual(titler(26), 'Z')

    def test_double(self):
        self.assertEqual(titler(27),'AA')
        self.assertEqual(titler(27),'AA')
        self.assertEqual(titler(701),'ZY')

def titler(i):
    output = []
    if i > 26:
        return ''.join([chr(64 + (i//26)), chr(64 + (i%26))])
    else:
        return chr(64 + i)

if __name__ == '__main__':
    unittest.main()
