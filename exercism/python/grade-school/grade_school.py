from collections import defaultdict

class School(object):
    def __init__(self, name):
        self.school = name
        self._grade = defaultdict(set)

    def add(self, name, grade):
        self._grade[grade].add(name)

    def grade(self, grade):
        return self._grade[grade]

    def sort(self):
        output = []
        for key in sorted(self._grade.keys()):
            output.append((key, tuple(self._grade[key])))
        return output
