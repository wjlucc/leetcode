#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (54.74%)
# Likes:    2402
# Dislikes: 88
# Total Accepted:    534.8K
# Total Submissions: 967.6K
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # tag 零等特殊值移动问题
        # 对于特殊值，无需记录，在数组后面补充即可
        index = 0
        for v in nums:
            if v != 0:
                nums[index] = v
                index += 1
        for i in range(index, len(nums)):
            nums[i] = 0


    # 首次解法，蠢啊
    def moveZeroes_origin(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # tag: 双指针
        # 从前向后遍历，一个指向非0，一个指向0值
        i = 0
        while i != len(nums):
            p_zero = self.nextZero(nums, i)
            if(p_zero == -1):
                break
            p_not_zero = self.nextNotZero(nums, i)
            if (p_not_zero == -1):
                break
            if(p_zero < p_not_zero):
                nums[p_zero], nums[p_not_zero] = nums[p_not_zero], nums[p_zero]
            i = p_zero
            
    def nextZero(self, nums, start):
        while start != len(nums) and nums[start] != 0:
            start += 1
        if (start != len(nums)):
            return start
        else:
            return -1
    
    def nextNotZero(self, nums, start):
        while start != len(nums) and nums[start] == 0:
            start += 1
        if (start != len(nums)):
            return start
        else:
            return -1
        
# @lc code=end

