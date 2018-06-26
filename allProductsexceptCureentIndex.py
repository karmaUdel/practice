import unittest


def get_products_of_all_ints_except_at_index(int_list):

    # Make a list with the products
    if len(int_list)<2:
        raise Exception
    
    fromLeft = 1
    fromRight = 1
    
    prodList = [1] * len(int_list)
    
    #go from left to end --> 1 a ab abc abcd ... till end
    i = 0
    for ints in int_list:
        prodList[i] = prodList[i] * fromLeft # keep same 
        fromLeft = fromLeft * ints # add currentIndexVal
        i +=1 # let i reach end
    # come back from right to start --> start .... ...xyz ....wyz ...wxy 
    i-=1 # set last index
    int_list.reverse() # don't forget to reverse the list
    for ints in int_list:
        prodList[i] = prodList[i] * fromRight # keep same 
        fromRight = fromRight * ints # add currentIndexVal
        i-=1 # reduce i

    return prodList


















# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)