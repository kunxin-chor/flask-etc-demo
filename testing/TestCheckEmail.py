import unittest
from func import check_valid_email

class TestCheckEmail(unittest.TestCase):
    def test_can_detect_add_symbol(self):
        self.assertTrue(check_valid_email("a@a.com"))       
        
    def test_can_detect_multiple_add_symbol(self):
        self.assertFalse(check_valid_email("a@a@a.com"))
        
    def test_can_detect_no_top_level_domain(self):
        self.assertFalse(check_valid_email('a@a.'))
        
    def test_can_detect_no_dot(self):
        self.assertFalse(check_valid_email("a@"))
    
    def test_can_detect_no_add_and_no_dot(self):
        return self.assertFalse(check_valid_email("a"))
        
    def test_can_detect_emtpy(self):
        return self.assertFalse(check_valid_email(""))
        
if __name__ == '__main__':
    unittest.main()