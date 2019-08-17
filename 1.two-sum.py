#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_value = {}
        for i in range(len(nums)):
            if target - nums[i] in index_value:
                return [index_value[target - nums[i]], i]
            index_value[nums[i]] = i

