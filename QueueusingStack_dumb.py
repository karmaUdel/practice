import unittest


class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self, item):
        if not self.stack1 :
            self.stack2.append(item)
        if not self.stack2 :
            self.stack1.append(item)
        #print (self.stack1)
        #print (self.stack2)

    def dequeue(self):
        #print (self.stack1)
        #print (self.stack2)
        if not self.stack1 :
            while self.stack2 : 
                self.stack1.append(self.stack2.pop())
            item = self.stack1.pop()
            while self.stack1 : 
                self.stack2.append(self.stack1.pop())
            return item
            
        if not self.stack2 :
            while self.stack1 : 
                self.stack2.append(self.stack1.pop())
            item = self.stack2.pop()
            while self.stack2 : 
                self.stack1.append(self.stack2.pop())
            return item



















# Tests

class Test(unittest.TestCase):

    def test_queue_usage(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)