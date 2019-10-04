#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (32.50%)
# Likes:    705
# Dislikes: 2079
# Total Accepted:    416.1K
# Total Submissions: 1.3M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool: 
        # tag 利用python字符串和list特性
        # python 特性可能会增加时延也可能减少时延
        # python 字符串大写: str.upper()，小写: str.lower()
        # str.isalnum() 直接判断字符是不是个字母或者数字
        # join 可以拼接整个list
        if len(s) == 0:
            return True
        
        i,j = 0, len(s) - 1
        s = s.lower()
        data_base = set("abcdefghijklmnopqrstuvwxyz0123456789")
        while(i < j):
            while(i < len(s) and (s[i] not in data_base)):
                i += 1            
            while(j >= 0 and (s[j] not in data_base)):
                j -= 1
            if i < j and s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
    
    def isPalindromeOther(self, s: str) -> bool:
        s = "".join([ i for i in s.lower() if i.isalnum() ])
        return s == s[::-1]
               
# @lc code=end

