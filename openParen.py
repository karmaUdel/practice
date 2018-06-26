import unittest


def get_closing_paren1(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    stack = []
    expectEnd = -1
    counter = 1
    i = 0
    for ch in sentence:
        #print ch == '('
        if ch == '(':
            stack.append(ch)
            if expectEnd > 0:
                expectEnd +=1
                counter+=1
        if ch == ')':
            stack.pop()
            if expectEnd > -1:
                #return i # matching end arrived
                print(expectEnd, counter)
                if counter == expectEnd :
                    return i
                else:
                    counter +=1
            #if expectEnd > 0:
            #    expectEnd-=1 # expect end soon
        if  i == opening_paren_index :
            expectEnd = len(stack)
            if ch == ')': # closing parenthesis
                raise Exception
        i +=1
    
    raise Exception


def get_closing_paren(sentence, opening_paren_index):
    stack = []
    i = 0
    expectEnd = -1
    other = -1
    for ch in sentence :
        if ch == '(':
            stack.append(ch)
            if expectEnd > 0 :
                other +=1 #extra open '('
        if ch ==')':
            stack.pop()
            if expectEnd > 0:
                if other == expectEnd:
                    return i
                else:
                    other -=1
        if i == opening_paren_index :
            expectEnd = len(stack) # current open '(' 
            other = expectEnd
        i +=1
    raise Exception 
# Tests


def get_closing_paren_Best(sentence, opening_paren_index):
    open_nested_parens = 0
    position = opening_paren_index + 1

    for position in xrange(opening_paren_index + 1, len(sentence)):
        char = sentence[position]

        if char == '(':
            open_nested_parens += 1
        elif char == ')':
            if open_nested_parens == 0:
                return position
            else:
                open_nested_parens -= 1

    raise Exception("No closing parenthesis :(")

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        print('------------')
        self.assertEqual(actual, expected)
        


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        print('------------')
        self.assertEqual(actual, expected)
        #print('------------')

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)
        #print('------------')


unittest.main(verbosity=2)