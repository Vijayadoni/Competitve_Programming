import unittest


def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError('invalid')

    max1 = max(list_of_ints[0], list_of_ints[1])
    least  = min(list_of_ints[0], list_of_ints[1])
    prod2 = list_of_ints[0] * list_of_ints[1]
    low  = list_of_ints[0] * list_of_ints[1]
    prod3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]
        prod3 = max(prod3,current * prod2,current * low)
        prod2 = max(prod2,current * max1,current * least)
        low = min(low,current * max1,current * least)
        max1 = max(max1, current)
        least = min(least, current)
        
    return prod3



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