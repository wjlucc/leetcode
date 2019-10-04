#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (53.69%)
# Likes:    866
# Dislikes: 117
# Total Accepted:    403K
# Total Submissions: 750.4K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t , write a function to determine if t is an anagram
# of s.
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # tag 元素出现数目
        # ！python list和str有count方法，可以返回出现次数！！ 
        # python在解决某些字符串问题很简单，会影响到思考方式      
        data_base = dict()        
        for v in s:
            if v in data_base:
                data_base[v][0] += 1
            else:
                data_base[v] = [1, 0]
        for v in t:
            if v not in data_base:
                return False
            else:
                data_base[v][1] += 1
                
        for k,v in data_base.items():
            if v[0] != v[1]:
                return False
        return True
        
# @lc code=end

