#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (60.82%)
# Likes:    2896
# Dislikes: 110
# Total Accepted:    537.9K
# Total Submissions: 873.4K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,1]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,1,2,1,2]
# Output: 4
# 
# 
#

# @lc code=start
class Solution:
    # tag 借用set数据结构
    # 注意题目线性复杂度可以，对内存无要求时可以使用外部结构
    # 若对空间有要求，不可以使用。
    # 不适用更多空间，且线性复杂度应该如何处理？
    def singleNumber(self, nums: List[int]) -> int:
        data_base = set()
        for v in nums:
            if (v in data_base):
                data_base.remove(v)
            else:
                data_base.add(v)
        return data_base.pop()  # 有多个元素时不要使用pop
                
        
        
# @lc code=end

