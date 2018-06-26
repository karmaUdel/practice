import unittest


def is_single_riffle(half1, half2, shuffled_deck):

    # Check if the shuffled deck is a single riffle of the halves
    h1max = len(half1)
    h2max = len(half2)
    h1 = 0
    h2 = 0
    for card in shuffled_deck:
        if h1< h1max and half1[h1] == card :
            h1+=1
        
        else : 
            if h2< h2max and half2[h2] == card :
                h2+=1
            else:
                return False
    return True


















# Tests

class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)