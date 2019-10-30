import unittest
from func import calculate_gst
class TestGSTCalculator(unittest.TestCase):
    
    def test_can_calculate_gst(self):
        self.assertAlmostEqual( calculate_gst(100), 7)
        self.assertAlmostEqual( calculate_gst(200), 14)

if __name__ == '__main__':
    unittest.main()
        
    