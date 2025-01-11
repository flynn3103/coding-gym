"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/

Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

"""

def minSubArrayLen(arr, target):
    # n = len(arr)
    # min_length = float("inf")
    # for start in range(n):
    #     current_sum = 0
    #     for end in range(start, n):
    #         current_sum += arr[end]
    #         if current_sum >= target:
    #             min_length = min(min_length, end - start + 1)
    #             break
    # return 0 if min_length == float("inf") else min_length
    n = len(arr)
    start, end =  0, 0
    min_len = float('inf')
    curr_sum = 0
    while end < n:
        curr_sum += arr[end]
        if curr_sum >= target:
            min_len = min(min_len, end - start + 1)
            curr_sum -= arr[start]
            start += 1
        end += 1
            
    return 0 if min_len == float('inf') else min_len
        

# Test cases
print(minSubArrayLen([2,3,1,2,4,3], 7))  # Should print 2
print(minSubArrayLen([1,4,4], 4))        # Should print 1