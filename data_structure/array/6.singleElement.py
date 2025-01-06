"""
Given an array of integers. All numbers occur twice except one number which occurs once. 
Find the number in O(n) time & constant extra space.

Question-driven:
Input Constraints:
- What is the maximum size of the array?
- Can the array be empty?
- Are there any constraints on the values of the integers in the array (e.g., range of values)?

Output Requirements:

- What should be the output if the array is empty?
- Should the function return the single element directly, or is there a specific format for the output?

Edge Cases:

- How should the function handle arrays with only one element?
- Are there any special cases we should consider, such as all elements being the same except one?
- Performance:

- Is there a specific time complexity requirement for the solution?
- Are there any constraints on the space complexity?


Example : 

Input:  arr[] = {2, 3, 5, 4, 5, 3, 4}
Output: 2 

Input:  arr[] = {2, 5, 2}
Output: 5

Input:  arr[] = {3}
Output: 3
"""


def singleElement(arr):
    # Brute force
    hashMap = {}
    for num in arr:
        if num in hashMap:
            hashMap[num] += 1
        else:
            hashMap[num] = 1
    
    for num in hashMap:
        if hashMap[num] == 1:
            return num
    return None


import unittest
class TestSingleElement(unittest.TestCase):
    def test_single_occurrence(self):
        self.assertEqual(singleElement([2, 3, 5, 4, 5, 3, 4]), 2)
    
    def test_single_occurrence_2(self):
        self.assertEqual(singleElement([2, 5, 2]), 5)
    
    def test_single_element(self):
        self.assertEqual(singleElement([3]), 3)
    
    def test_empty_array(self):
        self.assertEqual(singleElement([]), None)  # Assuming function returns None for empty array

if __name__ == '__main__':
    unittest.main()