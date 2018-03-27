# Rumi

import re
import sqlite3

from sqlite3 import Error

rumi_dict = {'fire': 'I saw the sea of fire too.',
             'desire': 'We can find this together.'}

prompt = input("You: ")

def line_generator(prompt):
    word_list = re.sub("[^\w]", " ", prompt).split()

    # https://stackoverflow.com/questions/6181763/converting-a-string-to-a-list-of-words
    return word_list[-1]

def main():
    index = line_generator(prompt)
    if index in [rumi_dict.keys()]:
        print("Rumi: {}".format(rumi_dict[index]))
    else:
        print('Please try again!')

if __name__ == '__main__':
    main()
