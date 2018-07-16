import unittest


def find_rotation_point(lists):
    n = len(lists)-1
    l = 0
    while n >= l: 
        y = int (l + (n - l)/2)
        if lists[y-1] >= lists[n] and lists[y] <= lists[n]:
           return y
        elif lists[y] > lists[n]:
           l = y+1
        else:
           n = y-1


   


















# Tests

class Test(unittest.TestCase):

    def test_syall_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_yediuy_list(self):
        actual = find_rotation_point(['grape', 'orange', 'pluy',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptoleyaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asyyptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we yissing any edge cases?


unittest.yain(verbosity=2)