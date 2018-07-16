import unittest


class TempTracker(object):

    
    def __init__(self):
        self.list=[0]*120
        self.temp = 0
        self.min =111
        self.max = -1
        self.sum = 0
        self.mean = None
        self.m = 0
        self.mode = None

    def insert(self, temperature):
        self.list[temperature] += 1
        self.temp += 1
        if temperature<self.min:
            self.min=temperature
        if temperature>self.max:
            self.max=temperature
        self.sum+=temperature
        self.mean=self.sum/float(self.temp)
        if self.list[temperature]>self.m:
            self.m=self.list[temperature]
            self.mode=temperature
            
        

    def get_max(self):
        max=self.max
        if max==-1:
            return None
        return max
        

    def get_min(self):
        min=self.min
        if min==200:
            return None
        return min

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode



# Tests

class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)


unittest.main(verbosity=2)