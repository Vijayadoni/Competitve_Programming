import unittest

def get_perm(string):
	# Generate all perm of the input string
	if(len(string)==0):
		return set([''])
	if (len(string) == 1):
		return set(string)
	tmp = string[0]
	rest = string[1:]
	perm_rest = get_perm(rest)
	perm = set()
	for w in perm_rest:
		for p in range(len(rest) + 1):
			perm.add(w[:p] + tmp + w[p:])
	return perm

# Tests

class Test(unittest.TestCase):

	def test_empty_string(self):
		actual = get_perm('')
		expected = set([''])
		self.assertEqual(actual, expected)

	def test_one_character_string(self):
		actual = get_perm('a')
		expected = set(['a'])
		self.assertEqual(actual, expected)

	def test_two_character_string(self):
		actual = get_perm('ab')
		expected = set(['ab', 'ba'])
		self.assertEqual(actual, expected)

	def test_three_character_string(self):
		actual = get_perm('abc')
		expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
		self.assertEqual(actual, expected)


unittest.main(verbosity=2)