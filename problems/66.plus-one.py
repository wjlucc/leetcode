#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (41.50%)
# Likes:    1006
# Dislikes: 1780
# Total Accepted:    450.6K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# 
# Example 2:
# 
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# 
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 简单题，用最直观解法去处理
        flag = 0
        for i in range(len(digits) - 1, -1, -1):
            flag = self.plus(digits, i)
            if (flag == 0):
                return digits
        if(flag == 1):
            digits.insert(0, 1)
        return digits
        
            
            
    def plus(self, digits: List[int], index: int) -> int:
        digits[index] += 1
        flag = 0
        if (digits[index] == 10):
            digits[index] = 0
            flag = 1
        else:
            flag = 0
        return flag
        
# @lc code=end

