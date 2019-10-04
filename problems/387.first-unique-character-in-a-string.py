#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (50.73%)
# Likes:    1208
# Dislikes: 87
# Total Accepted:    325K
# Total Submissions: 640.6K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # tag 需要先遍历一遍
        # !!! 字符串个数是有限的，可以只遍历一次有限的字符串
        # str.find() 和 str.rfind() 分别从左右查找
        data_base = dict()
        for v in s:
            if v not in data_base:
                data_base[v] = 1
            else:
                data_base[v] += 1
                
        for i, v in enumerate(s):
            if (data_base[v] == 1):
                return i            
        return -1
    
    def firstUniqCharOther(self, s: str) -> int:
        # 其他人的解法
        index = len(s)
        for c in "abcdefghijklmnopqrstuvwxyz":
            i = s.find(c)
            if (i != -1 and i == s.rfind(c)):
                index = min(index, i)
        return index if index < len(s) else -1
        
# @lc code=end

