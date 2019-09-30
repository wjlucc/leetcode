#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 使用双指针
        if (len(nums) <= 1):
            return len(nums)
        
        start = 0
        for end in range(1, len(nums)):
            if (nums[end] != nums[end-1]):
                start += 1
                nums[start] = nums[end]
        return start+1
   

