import unittest


def approach1(the_list):
    lsi = {}
    for num in the_list:
        if num in lsi:
            return num
        else:
            lsi[num] = 1

    return 0
    
def find_repeat1(the_list):

    # Find a number that appears more than once
    
    list.sort(the_list)
    for i in range(0, len(the_list)-1,1):
        if the_list[i] == the_list[i+1]:
            return the_list[i]

    return 0


def find_repeat(numbers_list):
	#O(n) and O(1) space
    # Find the number that appears twice
    for i in range(0, len(numbers_list)):
        if numbers_list[abs(numbers_list[i])] >= 0:
            numbers_list[abs(numbers_list[i])] = - numbers_list[abs(numbers_list[i])]
        else:
            return abs(numbers_list[i])

    return 0


# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)