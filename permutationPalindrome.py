import unittest


def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    chars = list(the_string)
    charMap = {}
    for char in chars:
        if char in charMap:
            charMap[char] +=1
        else:
            charMap[char] = 1
    odds = 0    
    for key in charMap.keys():
        if not(charMap[key]%2 == 0):
            odds +=1
    if odds <=1 :
        return True
    return False


















# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)