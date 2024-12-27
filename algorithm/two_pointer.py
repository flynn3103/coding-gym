"""
Key things to remember when using two pointers:

Always check array bounds to avoid index out of range errors
Consider sorting the array first if order doesn't matter
Be careful with duplicates if they need to be handled specially
Think about whether the pointers should move in the same or opposite directions
Consider whether the pointers should move at the same or different speeds
"""
def findPairWithSum(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []  # No pair found

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(findPairWithSum(nums, target))  # Output: [0, 1]
