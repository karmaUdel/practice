import unittest


def highest_product_of_3(list_of_ints):

    # Calculate the highest product of three numbers
    if len(list_of_ints) <3:
        raise Exception
    mx1 = -1000000
    mx2 = -1000000
    mx3 = -1000000
    mn2 = 1000000
    mn3 = 1000000
    for ints in list_of_ints:
        if mx1 <ints:
            mx1 = ints
        if mn2 > ints:
            mn2 = ints
    
    list_of_ints.remove(mx1)
    list_of_ints.remove(mn2)
    for ints in list_of_ints:
        if mx2 <ints:
            mx2 = ints
        if mn3 > ints:
            mn3 = ints
    list_of_ints.remove(mx2)
    for ints in list_of_ints:
        if mx3 <ints:
            mx3 = ints
    return max(mx1*mx2*mx3, mx1*mn2*mn3)
    return 0


















# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)