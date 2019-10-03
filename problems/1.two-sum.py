#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (44.34%)
# Likes:    11317
# Dislikes: 389
# Total Accepted:    2M
# Total Submissions: 4.4M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # tag: 借用map结构辅助
        # ！！！ 遍历list时使用enumerate，速度更快
        datas = dict()
        for i, v in enumerate(nums):
            if v in datas:
                return [datas[v], i]
            else:
                key = target - nums[i]  
                datas[key] = i  
                
        '''
        for i in range(len(nums)):
            if nums[i] in datas:
                return [datas[nums[i]], i]
            else:
                key = target - nums[i]  
                datas[key] = i            
        
        '''

# @lc code=end

