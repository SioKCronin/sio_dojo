import unittest
import string

def higher_or_equal(operator):
    return True

PRECEDENCE = {
        '*':3, 
        '/':3, 
        '+':2,
        '-':2,
        '(':1
}

CHARACTERS = string.ascii_uppercase
DIGITS = string.digits
LEFT_PAREN = '('
RIGHT_PAREN = ')'

def to_postfix(infix_expression):
    operation_stack = []
    postfix = []
    tokens = list(infix_expression)
    for token in tokens:
        if token in CHARACTERS or token in DIGITS:
            postfix.append(token)
        elif token == LEFT_PAREN:
            operation_stack.append(token)
        elif token == RIGHT_PAREN:
            top_token = operation_stack.pop()
            while top_token != LEFT_PAREN:
                postfix.append(top_token)
                top_token = operation_stack.pop()
        else:
            while operation_stack and \
                    (PRECEDENCE[operation_stack[-1]] >= PRECEDENCE[token]):
                postfix.append(operation_stack.pop())
            operation_stack.append(token)

    operation_stack.reverse()
    postfix.extend(operation_stack)
    return ''.join(postfix)


class TestPostfix(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(to_postfix("A*B+C*D"), "AB*CD*+")

if __name__ == '__main__':
    unittest.main()
