import unittest
import os
print(os.getcwd())
from algorithm.two_pointer import findPairWithSum

class TestFindPairWithSum(unittest.TestCase):
    def test_pair_found(self):
        self.assertEqual(findPairWithSum([2, 7, 11, 15], 9), [0, 1])
    
    def test_pair_not_found(self):
        self.assertEqual(findPairWithSum([2, 7, 11, 15], 10), [])
    
    def test_empty_list(self):
        self.assertEqual(findPairWithSum([], 9), [])
    
    def test_single_element(self):
        self.assertEqual(findPairWithSum([2], 2), [])
    
    def test_multiple_pairs(self):
        self.assertEqual(findPairWithSum([1, 2, 3, 4, 4, 5], 8), [2, 5])

if __name__ == '__main__':
    unittest.main()