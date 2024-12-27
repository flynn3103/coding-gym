import unittest
from algorithm.binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_element_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7), 6)
    
    def test_element_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), -1)
    
    def test_empty_array(self):
        self.assertEqual(binary_search([], 7), -1)
    
    def test_single_element_found(self):
        self.assertEqual(binary_search([7], 7), 0)
    
    def test_single_element_not_found(self):
        self.assertEqual(binary_search([7], 8), -1)
    
    def test_first_element(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)
    
    def test_last_element(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)

if __name__ == '__main__':
    unittest.main()