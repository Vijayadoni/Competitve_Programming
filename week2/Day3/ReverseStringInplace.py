import unittest


def reverse(li):
	# Reverse the input list of chars in place
	for i in range(len(li)//2):
		li[i],li[len(li)-i-1] = li[len(li)-i-1],li[i]
	return li


# Tests

class Test(unittest.TestCase):

	def test_empty_string(self):
		li = []
		reverse(li)
		expected = []
		self.assertEqual(li, expected)

	def test_single_character_string(self):
		li = ['A']
		reverse(li)
		expected = ['A']
		self.assertEqual(li, expected)

	def test_longer_string(self):
		li = ['A', 'B', 'C', 'D', 'E']
		reverse(li)
		expected = ['E', 'D', 'C', 'B', 'A']
		self.assertEqual(li, expected)


unittest.main(verbosity=2)

















# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        li = []
        reverse(li)
        expected = []
        self.assertEqual(li, expected)

    def test_single_character_string(self):
        li = ['A']
        reverse(li)
        expected = ['A']
        self.assertEqual(li, expected)

    def test_longer_string(self):
        li = ['A', 'B', 'C', 'D', 'E']
        reverse(li)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(li, expected)


unittest.main(verbosity=2)