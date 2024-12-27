"""
Key points to remember when using sliding window:

Window Size:

Fixed size: Know your window size beforehand
Variable size: Use conditions to expand/contract window


Window State:

Track what's needed (sum, count, etc.)
Consider using hash maps for character frequencies


Window Movement:

Add new elements (right pointer)
Remove elements when needed (left pointer)
Update state accordingly


Optimization:

Only store what's necessary in the window
Consider using Counter for frequency problems
Remove unnecessary comparisons

"""
def findMaxAverage(nums, k):
    # Initialize window sum with first k elements
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    
    # Slide window
    for i in range(k, len(nums)):
        curr_sum = curr_sum + nums[i] - nums[i-k]  # Add new element, remove first element
        max_sum = max(max_sum, curr_sum)
    
    return max_sum / k

# Example usage:
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(nums, k))  # Output: 12.75