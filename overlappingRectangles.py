import unittest


def find_rectangular_overlap(rect1, rect2):

    # Calculate the overlap between the two rectangles
    left = {}
    right = {}
    #lapPossible = False
    overlap = {
        'left_x': None,
        'bottom_y': None,
        'width': None,
        'height': None,
    }
    if rect1['left_x'] <=rect2['left_x']:
        #rect1 is to left of rect 2
        left = rect1
        right = rect2
    else:
        #rect1 is to left of rect 2
        left = rect2
        right = rect1
    
    if not(left['bottom_y'] < right['bottom_y']+right['height']) :#and right[bottom_y]+right[height] <= left[bottom_y]+left[height] :
    #   left is below right
        #lapPossible = True
    #else:
    #   right is below left
    #   and no intesection so return empty
        return overlap
    if left['left_x']+left['width'] >right['left_x'] : #and lapPossible :
        overlap['left_x'] =right['left_x']
        if left['left_x']+left['width'] >right['left_x']+right['width'] :
            overlap['width'] = right['width'] # left is bigger than right
        else:
            overlap['width'] = left['left_x']+left['width'] - right['left_x']
            # right is bigger than left
    else:
        #no overlap
        return overlap
    
    if left['bottom_y'] > right['bottom_y'] :
        overlap['bottom_y']= left['bottom_y']
        if left['bottom_y'] + left['height'] < right['bottom_y']+ right['height'] :
            overlap['height']= left['height'] # left is smaller in height to right rectangle
        else:
            overlap['height'] = right['bottom_y']+ right['height'] - left['bottom_y']
    else: #right rectangle is above left 
        overlap['bottom_y']= right['bottom_y']
        if right['bottom_y']>= left['bottom_y']+left['height']: # left is below right and not touching
            # no overlap
            return {'left_x': None,'bottom_y': None,'width': None,'height': None,}
        else:
            if right['bottom_y'] + right['height'] < left['bottom_y']+ left['height'] :
                overlap['height']= right['height'] # right is smaller in height to left rectangle
            else:
                overlap['height'] = left['bottom_y']+ left['height'] - right['bottom_y']
                #overlap[height'] = left[bottom_y']+left['height'] - right['bottom']
    return overlap

# Tests

class Test(unittest.TestCase):

    def test_overlap_along_both_axes(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 3,
        }
        rect2 = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 3,
            'height': 6,
        }
        expected = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 2,
            'height': 2,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)


    def test_one_rectangle_inside_another(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 6,
        }
        rect2 = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_both_rectangles_the_same(self):
        rect1 = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        rect2 = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        expected = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_on_horizontal_edge(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 3,
            'height': 4,
        }
        rect2 = {
            'left_x': 2,
            'bottom_y': 6,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_on_vertical_edge(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 3,
            'height': 4,
        }
        rect2 = {
            'left_x': 4,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_at_a_corner(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rect2 = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_no_overlap(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rect2 = {
            'left_x': 4,
            'bottom_y': 6,
            'width': 3,
            'height': 6,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)