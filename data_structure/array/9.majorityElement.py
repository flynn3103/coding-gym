"""
https://leetcode.com/problems/majority-element/
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than [n / 2] times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

def majorityElement(arr): 
    major_num = len(arr) // 2
    # O(n^2)
    # for i in range(len(arr)):
    #     counter = 0
    #     for j in range(i, len(arr)):
    #         if arr[i] == arr[j]:
    #             counter += 1
    #     if counter >= major_num:
    #         return arr[j]
    # O(n)
    hashMap = {}
    for num in arr:
        hashMap[num] = hashMap.get(num, 0) + 1
        if hashMap[num] > major_num:
            return num

arr = [2,2,1,1,1,2,2]
print(majorityElement(arr))

