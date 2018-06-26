import unittest

mem = {}
def fib(n):

    # Compute the nth Fibonacci number
    if n == 0 or n ==1:
        return n
    if n < 0:
        raise Exception
    
    result =  fib(n-1)+ fib (n-2)
    mem[n] = result
    return result
    #return -1






MAX = 1000
 
# Create an array for memoization
f = [0] * MAX
 
# Returns n'th fuibonacci number using table f[]
def fib_better(n) :
    # Base cases
    if (n == 0) :
        return 0
    if (n == 1 or n == 2) :
        f[n] = 1
        return (f[n])
 
    # If fib(n) is already computed
    if (f[n]) :
        return f[n]
 
    if( n & 1) :
        k = (n + 1) // 2
    else : 
        k = n // 2
 
    # Applyting above formula [Note value n&1 is 1
    # if n is odd, else 0.
    if((n & 1) ) :
        f[n] = (fib_better(k) * fib_better(k) + fib_better(k-1) * fib_better(k-1))
    else :
        f[n] = (2*fib_better(k-1) + fib_better(k))*fib_better(k)
 
    return f[n]
 











# Tests

class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


unittest.main(verbosity=2)