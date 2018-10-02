import string

def is_pangram(s):
    s = sorted(set([i.lower() for i in s if i.isalpha()]))
    alpha = list(string.ascii_lowercase)
    if len(s) != len(alpha):
        return False
    for i, char in enumerate(s):
        if char != alpha[i]:
            return False
    return True
