import unittest
from func import add_two

    
# inheriting from unittest.TestCase
class TestAddTwoNumbers(unittest.TestCase):
    
    def test_add_2_to_2_gives_4(self):
        # a test is defined with an assert statement
        self.assertEqual(add_two(2,2), 4)
        
    def test_add_2_to_string(self):
        self.assertEqual(add_two("2", 2), 4)
        
    def test_add_2_to_two(self):
        self.assertEqual(add_two("two", 2), None)
    
if __name__ == '__main__':
    unittest.main()