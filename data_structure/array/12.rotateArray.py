def rotateArray(nums, k):
    """
    https://leetcode.com/problems/rotate-array/description/

    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

    Example 1:

    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]

    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]

    Example 2:
    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]
    Explanation: 
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]
    """
    # n = len(arr)

    # for _ in range(k):
    #     previous = arr[-1]
    #     for i in range(n):
    #         arr[i], previous = previous, arr[i]
    # return arr
    # Approach 2: Time O(n), space O(1)
    k = k % len(nums)
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    
    left, right = 0, k - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    
    left, right = k, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    


def test_rotateArray():
    assert rotateArray([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert rotateArray([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
    assert rotateArray([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
    assert rotateArray([1, 2, 3], 4) == [3, 1, 2]

if __name__ == "__main__":
    test_rotateArray()
    print("All tests passed.")
