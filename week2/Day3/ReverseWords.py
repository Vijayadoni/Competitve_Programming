import unittest


def reverse_words(msg):

	# Decode the msg by reversing the words
	l = []
	word = ''
	
	for i in range(len(msg)):
		if(msg[i]!=' '):
			word = word+msg[i]
		else:
			l.append(word)
			word = ''

	l.append(word)

	for i in range(len(l)//2):		
		l[i],l[len(l)-i-1] = l[len(l)-i-1],l[i]
	count = 0
	for i in l:
		for j in i:
			msg[count] = j
			count += 1
		if(count!=len(msg)):
			msg[count] = ' '
			count += 1




# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)