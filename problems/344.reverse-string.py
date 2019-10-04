#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (64.18%)
# Likes:    889
# Dislikes: 566
# Total Accepted:    506.2K
# Total Submissions: 788.7K
# Testcase Example:  '["h","e","l","l","o"]'
#
# Write a function that reverses a string. The input string is given as an
# array of characters char[].
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# You may assume all the characters consist of printable ascii characters.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# 
# 
# 
# Example 2:
# 
# 
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        # tag: 遍历前一半
        # 直接遍历得结果，需要注意不同语言表示的字符串不同，c++ 如何求length？数组长度直接size()
        # 可能传来的是个str类型。python list和str类型操作很类似。可以直接使用 l[::-1] 对l求逆，l可以是list或者str
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        mid = length // 2
        for i in range(mid):
            s[i], s[length - i - 1] = s[length - i - 1], s[i]       
# @lc code=end

