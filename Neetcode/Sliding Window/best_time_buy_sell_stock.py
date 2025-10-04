"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

# Using Brute force Approach O(n*2)
# def MaxProfit(prices):
#     res = 0
#     for i in range(len(prices)):
#         buy = prices[i]
#         for j in range(i+1, len(prices)):
#             sell = prices[j]
#             res = max(res, sell-buy)
#     return res

# prices = [7,1,5,3,6,4]
# print(MaxProfit(prices))


# # Using two pointers O(n)
# def maxProfit(prices):
#     left = 0
#     right = 1
#     maxP = 0

#     while right<len(prices):
#         if prices[left]<prices[right]:
#             profit = prices[right]-prices[left]
#             maxP = max(maxP,profit)
#         else:
#             left = right
#         right = right + 1
#     return maxP
            
# prices = [7,1,5,3,6,4]
# print(maxProfit(prices))



# def maxProfit(prices):
#     left = 0
#     right = 1
#     maxP = 0 

#     while right<len(prices):
#         if prices[left]<prices[right]:
#             profit = prices[right]-prices[left]
#             maxP = max(profit,maxP)
#         else:
#             left = right
#         right = right + 1
#     return maxP

# prices = [7,1,5,3,6,4]
# print(maxProfit(prices))


def maxProfit(prices):
    left = 0
    right = 1
    maxP = 0

    while right<len(prices):
        if prices[left]<prices[right]:
            profit = prices[right]-prices[left]
            maxP = max(profit,maxP)
        else:
            left =right
        right = right + 1
    return maxP


