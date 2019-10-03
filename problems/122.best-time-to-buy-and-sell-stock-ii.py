#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# algorithms
# Easy (52.55%)
# Likes:    1267
# Dislikes: 1422
# Total Accepted:    377.8K
# Total Submissions: 710.3K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times).
# 
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
# 
# Example 1:
# 
# 
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit =
# 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 =
# 3.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are
# engaging multiple transactions at the same time. You must sell before buying
# again.
# 
# 
# Example 3:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # tag: 双指针
        # 分别标志买/卖
        if (len(prices) <= 1):
            return 0
        
        sum_profit = 0
        start = -1
        for end in range(1, len(prices)):
            # 当前无股票，考虑是否买前一个
            if (start == -1):
                if (prices[end] > prices[end - 1]):
                    start = end - 1     
            
            # 当前有股票，考虑是否卖
            if (start != -1):
                if (prices[end] > prices[end - 1]):
                    sum_profit += prices[end] - prices[end - 1]
                    start = -1
        return sum_profit
# @lc code=end

