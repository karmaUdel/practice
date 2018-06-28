import unittest
import heapq

class TempTracker(object):

    # Implement methods to track the max, min, mean, and mode
    
    def __init__(self):
        self.heap = []
        self.mean = 0
        self.mode = 0

    def insert(self, temperature):
        heapq.heappush(self.heap,temperature)
        self.mean = float((self.mean * (len(self.heap) - 1))+ temperature)/len(self.heap)
        self.mode = int(self.heap[-1] - self.heap[0])
    
    def get_max(self):
        if self.heap :
            return self.heap[-1]
        else:
            raise Exception

    def get_min(self):
        if self.heap :
            return self.heap[0]
        else:
            raise Exception

    def get_mean(self):
        if self.heap:
            print(self.mean)
            return self.mean
        else :
            raise Exception

    def get_mode(self):
        if self.heap:
            #self.mode = self.heap[-1]- self.heap[0]
            #mode has issues, need to fix it
			print (self.mode)
            return self.mode
        else :
            raise Exception


















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