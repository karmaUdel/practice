import unittest

def opener(ch):
    l = ['{','[','(']
    if ch in l:
        return True
    return False

#returns true if not matched close {/[/(
def bad(item,ch):
    if (ch == ']' and item == '[' )or (ch == ')' and item == '(' ) or (ch == '}' and item == '{' ) :
        return False
    return True

def is_valid(code):

    # Determine if the input code is valid
    stack = []
    for ch in code:
        if opener(ch) :
            stack.append(ch)
        else :
            if not stack :
                return False
            item = stack.pop()
            if bad(item, ch):
                return False
            
    if not stack :
        return True
    else:
        return False



# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)