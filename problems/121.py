"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


# Brute force, Time: O(n^2)
# def maxProfit(prices: list[int]) -> int:
#     maxProfit = 0
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[j] - prices[i] > maxProfit:
#                 maxProfit = prices[j] - prices[i]
#     return maxProfit


# Sliding window
# This was some voodo shit
# def maxProfit(prices: list[int]) -> int:
#     if len(prices) == 1:
#         return 0
#
#     maxProfit = 0
#     windowEnd = 1
#     for windowStart in range(len(prices)):
#         profit = prices[windowEnd] - prices[windowStart]
#         maxProfit = max(profit, maxProfit)
#         while windowEnd < len(prices) - 1 and prices[windowEnd] >= prices[windowStart]:
#             profit += prices[windowEnd + 1] - prices[windowEnd]
#             windowEnd += 1
#             maxProfit = max(profit, maxProfit)
#
#     return maxProfit


def maxProfit(prices: list[int]) -> int:
    maxProfit = 0
    l, r = 0, 1

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        else:
            l = r
        r += 1

    return maxProfit


print(f"Profit for [7,1,5,3,6,4] is {maxProfit([7, 1, 5, 3, 6, 4])}")
print(f"Profit for [7,6,4,3,1] is {maxProfit([7, 6, 4, 3, 1])}")
print(f"Profit for [1, 2] is {maxProfit([1, 2])}")
print(f"Profit for [1, 2, 4] is {maxProfit([1, 2, 4])}")
