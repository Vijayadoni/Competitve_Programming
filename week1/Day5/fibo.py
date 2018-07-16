import unittest


def fib(n):

    temp = [0, 1]
    if n < 0:
        raise ValueError("invalid")     
    while len(temp) < n + 1: 
        temp.append(0)      
    if n <= 1:
       return n
    else:
       if temp[n - 1] ==  0:
           temp[n - 1] = fib(n - 1)
     
       if temp[n - 2] ==  0:
           temp[n - 2] = fib(n - 2)
     
       temp[n] = temp[n - 2] + temp[n - 1]
    return temp[n]
    

    


















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