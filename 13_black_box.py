import unittest

def addition(num_1, num_2):
    return(num_1 + num_2)

class BlackBoxTest(unittest.TestCase):

    def test_sum_two_positive_num(self):
        num_1 = 10
        num_2 = 5

        result = addition(num_1, num_2)
        
        self.assertEqual(result, 15)

    def test_sum_two_negative_numbers(self):
        num_1 = -10
        num_2 = -7

        result = addition(num_1, num_2)
        
        self.assertEqual(result, -17)

if __name__ == '__main__':
    unittest.main() 
    
    
""" 
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()

 """