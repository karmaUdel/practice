import unittest



def sort_scores(unsorted_scores, highest_possible_score):
    # List of 0's at indices 0...highest_possible_score
    num_counts = [0] * (highest_possible_score + 1)

    # Populate num_counts
    for item in unsorted_scores:
        num_counts[item] += 1

    # Populate the final sorted list
    sorted_list = []

    # For each item in num_counts
    for item, count in enumerate(num_counts):

        # For the number of times the item occurs
        for _ in range(count):

            # Add it to the sorted list
            sorted_list.append(item)

    return sorted_list[::-1]






# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)