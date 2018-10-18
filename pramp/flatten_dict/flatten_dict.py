'''
Given a dictionary dict, write a function flattenDictionary that returns a 
flattened version of it .
'''
import unittest

class TestFlattenDict(unittest.TestCase):

    def test_pramp_example(self):
        input_dict = {
                    "Key1" : "1",
                    "Key2" : {
                        "a" : "2",
                        "b" : "3",
                        "c" : {
                            "d" : "3",
                            "e" : {
                                "" : "1"
                            }
                        }
                    }
                    }

        output_dict = {
                        "Key1" : "1",
                        "Key2.a" : "2",
                        "Key2.b" : "3",
                        "Key2.c.d" : "3",
                        "Key2.c.e" : "1"
                      }
        self.assertEqual(flattenDictionary(input_dict), output_dict)

output = {}

'''
def flatten_dict(dictionary):
  if type(dictionary) is not dict:
    return key, dictionary[key]

  for parent_key in dictionary.keys():
    if type(dictionary[parent_key]) == dict:
        for child_key, child_val in list(flatten_dict(dictionary[parent_key]).items()):
            if child_key:
                output["{}.{}".format(parent_key, child_key)] = child_val
            else:
                output["{}".format(parent_key)] = child_val
    else:
      output[parent_key] = dictionary[parent_key]

  return output
'''

def flattenDictionary(d):
    flatDictionary = {}
    flattenDictionaryHelper("", d, flatDictionary)

    return flatDictionary


def flattenDictionaryHelper(initialKey, d, flatDictionary):
    for key in d.keys():
        value = d[key]

        if not isinstance(value, dict): 
            if (initialKey == None or initialKey == ""):
                flatDictionary[key] = value
            else:
                flatDictionary[initialKey + "." + key] = value
        else:
            if (initialKey == None or initialKey == ""):
                flattenDictionaryHelper(key, value, flatDictionary)
            else:
                flattenDictionaryHelper(initialKey + "." + key, value, flatDictionary)


if __name__ == '__main__':
    unittest.main()

