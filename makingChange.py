import unittest

def recurse(amount,denomination,size):
    if amount == 0 :
        return 1
    if amount < 0 :
        return 0
    
    if size<=0 and amount >=1:
        return 0
    
    return recurse(amount,denomination,size-1)+recurse(amount - denomination [size-1], denomination, size)
    
def iterateWithMemory(amount,denomination,size):
    mem = [0 for i in range(0,amount+1)]
    mem[0]= 1 #base case
    for coin in denomination:
        for intermediate in range(coin, amount+1):
            mem[intermediate] += mem[intermediate - coin]
    return mem[amount]

def change_possibilities(amount, denominations):

    # Calculate the number of ways to make change
    
    #return recurse(amount,denominations,len(denominations))
    return iterateWithMemory(amount,denominations,len(denominations))





# Tests

class Test(unittest.TestCase):

    def test_sample_input(self):
        actual = change_possibilities(4, (1, 2, 3))
        expected = 4
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = change_possibilities(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = change_possibilities(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = change_possibilities(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = change_possibilities(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        actual = change_possibilities(100, (1, 5, 10, 25, 50))
        expected = 292
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)