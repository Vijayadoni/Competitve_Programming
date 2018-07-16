import unittest
 
def merge_ranges(array):
	maxi=0
	mylist = [0] * 48
	res = []
	for y in range(len(array)):
		x = array[y]
		if not (mylist[x[0]]) :
			mylist[x[0]]=x[1]
			maxi = max(maxi,x[1])
		elif mylist[x[0]] < x[1]:
			mylist[x[0]]=x[1]
			maxi = max(maxi,x[1])
	x = 0
	first = False
	for y in range(maxi+2):		
		if mylist[y] != 0:			
			if x == 0:
				if y == 0:
					first = True
				x = y				
		else:
			if x == 0 and first:
				res.append((x,max(mylist[x:y])))
				x = 0
				first = False
			elif x != 0:				
				res.append((x,max(mylist[x:y])))
				x = 0
	y=0
	result = []
	temp = -1
	for i in range(len(res)):
		if temp == -1:
			temp = res[i][0]
		y = res[i][1]
		if (i+1) != len(res):
			if y < res[i+1][1] and y >= res[i+1][0]:
				y = res[i+1][1]
			elif y >= res[i+1][1]:
				y = y
			else:
				result.append((temp,y))
				temp = -1
		else:
			result.append((temp,y))
	return result

# Tests

class Test(unittest.TestCase):

   def test_meetings_overlap(self):
       actual = merge_ranges([(1, 3), (2, 4)])
       expected = [(1, 4)]
       self.assertEqual(actual, expected)

   def test_meetings_touch(self):
       actual = merge_ranges([(5, 6), (6, 8)])
       expected = [(5, 8)]
       self.assertEqual(actual, expected)

   def test_meeting_contains_other_meeting(self):
       actual = merge_ranges([(1, 8), (2, 5)])
       expected = [(1, 8)]
       self.assertEqual(actual, expected)

   def test_meetings_stay_separate(self):
       actual = merge_ranges([(1, 3), (4, 8)])
       expected = [(1, 3), (4, 8)]
       self.assertEqual(actual, expected)

   def test_multiple_merged_meetings(self):
       actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
       expected = [(1, 8)]
       self.assertEqual(actual, expected)

   def test_meetings_not_sorted(self):
       actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
       expected = [(1, 4), (5, 8)]
       self.assertEqual(actual, expected)

   def test_sample_input(self):
       actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
       expected = [(0, 1), (3, 8), (9, 12)]
       self.assertEqual(actual, expected)


unittest.main(verbosity=2)

