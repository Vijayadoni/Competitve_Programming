import unittest


def has_palindrome_permutation(the_string):
	# Check if any permutation of the input is a palindrome
	d={}
	flag=1
	for i in the_string:		
		if i in d:
			d[i]+=1
		else:
			d[i]=1
	for i in d:
		if d[i]%2!=0:
			if(len(the_string)%2!=0):
				if flag==1:
					flag=0
					continue
			return False
	return True


# Tests

class Test(unittest.TestCase):

	def test_permutation_with_odd_number_of_chars(self):
		result = has_palindrome_permutation('aabcbcd')
		self.assertTrue(result)

	def test_permutation_with_even_number_of_chars(self):
		result = has_palindrome_permutation('aabccbdd')
		self.assertTrue(result)

	def test_no_permutation_with_odd_number_of_chars(self):
		result = has_palindrome_permutation('aabcd')
		self.assertFalse(result)

	def test_no_permutation_with_even_number_of_chars(self):
		result = has_palindrome_permutation('aabbcd')
		self.assertFalse(result)

	def test_empty_string(self):
		result = has_palindrome_permutation('')
		self.assertTrue(result)

	def test_one_character_string(self):
		result = has_palindrome_permutation('a')
		self.assertTrue(result)


unittest.main(verbosity=2)