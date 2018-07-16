import unittest


def get_closing_paren(strr, ind):
	# Find the position of the matching closing parenthesis
	o = 0
	r = 0
	if ( ind + 1 <= len(strr)-1 ):
		for i in range( ind + 1, len(strr) ):
			if strr[i] == '(':
				o = o+1
			else:
				o = o-1
			r = r+1
			if o < 0:
				return ind+r
	raise Exception


















# Tests

class Test(unittest.TestCase):

	def test_all_os_then_closers(self):
		actual = get_closing_paren('((((()))))', 2)
		expected = 7
		self.assertEqual(actual, expected)


	def test_mixed_os_and_closers(self):
		actual = get_closing_paren('()()((()()))', 5)
		expected = 10
		self.assertEqual(actual, expected)

	def test_no_matching_closer(self):
		with self.assertRaises(Exception):
			get_closing_paren('()(()', 2)


unittest.main(verbosity=2)














# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)