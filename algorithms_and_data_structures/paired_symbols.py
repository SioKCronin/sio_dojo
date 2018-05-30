PAIRINGS = {'(':')', '{':'}', '[':']'}

def is_balanced(symbols):
    stack = []
    for s in symbols:
        if s in PAIRINGS.keys():
            stack.append(s)
            continue
        try:
            expected_opening_symbol = stack.pop()
        except IndexError:
            return False
        if s != PAIRINGS[expected_opening_symbol]:
            return False
    return len(stack) == 0
