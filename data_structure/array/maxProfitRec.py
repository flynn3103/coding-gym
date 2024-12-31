"""
Given an array prices[] of size n denoting the cost of stock on each day,
the task is to find the maximum total profit if we can buy and sell the stocks any number of times.
Input: prices[] = {4, 2, 2, 2, 4}
Output: 2
Explanation: Buy the stock on day 3 and sell it on day 4 => 4 - 2 = 2
                       Maximum Profit  = 2
"""

# def maximumProfit(prices):
#     max_profit = 0
#     for i in range(len(prices)):
#         for j in range(i, len(prices)):
#             if prices[j] > prices[i]:
#                 profit = prices[j] - prices[i]
#                 max_profit = max(max_profit, profit)
#                 print(f"Buy on Day {i + 1} at price {prices[i]} and sell on Day {j + 1} at price {prices[j]} => Profit: {profit}")
    
#     print(f"Max profit = {max_profit}")
#     return max_profit

def maximumProfit(prices):
    """Optimize: Sliding Window Approach to Calculate Maximum Total Profit"""
    if not prices or len(prices) < 2:
        return 0

    total_profit = 0
    left, right = 0, 1
    n = len(prices)

    while right < n:
        curr_profit = prices[right] - prices[left]

        if curr_profit >= 0:
            # Accumulate the profit
            total_profit += curr_profit
            print(f"Buy on Day {left + 1} at price {prices[left]} and sell on Day {right + 1} at price {prices[right]} => Profit: {curr_profit}")
            # Move both pointers forward to look for next transaction
            left = right
            right += 1
        else:
            # If no profit, move the buy pointer to the sell pointer
            left = right
            right += 1

    return total_profit

# Driver Code
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(maximumProfit(prices))

