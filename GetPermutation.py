import unittest

def recurse(ch, string, permutation):
    if len(string) == 0 :
        return ch
    for char in string:
        s = string
        permutation.append(recurse(ch+char,s.replace(char, ""), permutation))
    print(permutation)
# problem with recursion
# appends None in list 
# fix it!!
def get_permutations(string):

    # Generate all permutations of the input string
    if not(string) :
        return set([''])
    permutation = []
    for ch in string:
        s = string
        permutation.append( recurse(ch,s.replace(ch, ""), permutation))
    permutation = [element for element in permutation if element is not None]
    return set(permutation)


















# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)