import unittest

class TestDecrypt(unittest.TestCase):

    def test_pramp_example1(self):
        self.assertEqual(decrypt("dnotq"), "crime")
        self.assertEqual(decrypt("flgxswdliefy"), "encyclopedia")

def decrypt(word):
  if len(word) == 0: return

  first = ord(word[0]) - 1
  while first < 97:
      first += 26

  output = ""
  output += chr(first)
  last_val = first + 1

  for letter in word[1:]:
    temp = ord(letter) - last_val
    last_val = ord(letter)
    while temp < 97:
      temp += 26
    output += chr(temp)

  return output

if __name__ == '__main__':
    unittest.main()
