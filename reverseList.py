import unittest


def reverse(head_of_list):

    # Reverse the linked list in place
    first = head_of_list
    last = None
    if first == None:
        return None
    if first.next == None :
        return first
    forward = first.next
    
    while first is not None:
        first.next = last
        last = first
        first = forward
        if first == None :
            break # first is none as last has reached last element
        forward = first.next 
    
    

    return last




# Tests

class Test(unittest.TestCase):

    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next  = next

        def get_values(self):
            node = self
            values = []
            while node is not None:
                values.append(node.value)
                node = node.next
            return values

    def test_short_linked_list(self):
        second = Test.LinkedListNode(2)
        first = Test.LinkedListNode(1, second)

        result = reverse(first)
        self.assertIsNotNone(result)

        actual = result.get_values()
        expected = [2, 1]
        self.assertEqual(actual, expected)

    def test_long_linked_list(self):
        sixth = Test.LinkedListNode(6)
        fifth = Test.LinkedListNode(5, sixth)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)

        result = reverse(first)
        self.assertIsNotNone(result)

        actual = result.get_values()
        expected = [6, 5, 4, 3, 2, 1]
        self.assertEqual(actual, expected)

    def test_one_element_linked_list(self):
        first = Test.LinkedListNode(1)

        result = reverse(first)
        self.assertIsNotNone(result)

        actual = result.get_values()
        expected = [1]
        self.assertEqual(actual, expected)

    def test_empty_linked_list(self):
        result = reverse(None)
        self.assertIsNone(result)


unittest.main(verbosity=2)