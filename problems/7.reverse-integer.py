#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.50%)
# Likes:    2493
# Dislikes: 3866
# Total Accepted:    821.7K
# Total Submissions: 3.2M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if (x < 10 and x > -10):
            return x
        
        # tag 数字转成str对于python更容易
        # list的操作可以直接用于str
        # python 求指数使用pow自带函数，可以直接用 ** 乘法表示pow
        # python list切片函数很好用！！！ l = list(range(10))[::3], l[::-1] 可以直接逆序！！！
        # s = '1234'，切片可以直接用于字符串！  s[::-1] 字符串逆序直接解
        x_str = str(x)
        result_str = ''
        if x_str[0] == '-':
            result_str += '-'
            
        result_str += x_str[::-1].lstrip('0').rstrip('-')
        result = int(result_str)
        if (result < -2 ** 31 or result > 2 ** 31 - 1):
            result = 0
        return result
        
        
        
    def reverse_origin(self, x: int) -> int:
        if (x < 10 and x > -10):
            return x      
        
        x_str = list(str(x))
        i, j = 0, len(x_str) - 1
        if (x_str[0] == '-'):
            i += 1
            
        while(i < j):
            x_str[i], x_str[j] = x_str[j], x_str[i]
            i += 1
            j -= 1        
        
        i, j = 0, len(x_str) - 1
        if (x_str[0] == '-'):
            i += 1
            
        while (i < len(x_str) and x_str[i] == '0'):
            i += 1
            
        result = 0
        m = 1
        for v in range(j, i - 1, -1):
            result += int(x_str[v]) * pow(10, len(x_str) - 1 - v)
            m *= 10
            
        
        if (x_str[0] == '-'):
            result *= -1

        if (result < pow(-2,31) or result > (pow(2,31) - 1)):
            result = 0
            
        return result
        
# @lc code=end

