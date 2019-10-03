#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (48.39%)
# Likes:    842
# Dislikes: 295
# Total Accepted:    242.4K
# Total Submissions: 492.7K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two arrays, write a function to compute their intersection.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# 
# 
# Note:
# 
# 
# Each element in the result should appear as many times as it shows in both
# arrays.
# The result can be in any order.
# 
# 
# Follow up:
# 
# 
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited such
# that you cannot load all elements into the memory at once?
# 
# 
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # tag 
        # 最简单的方式是用两个map
        # 拿到题后，先想最简单最直观的揭发，之后再考虑其他
        data_base = dict()
        for v in nums1:
            if v in data_base:
                data_base[v][0] += 1
            else:
                data_base[v] = [1, 0]

        for v in nums2:
            if v in data_base:
                data_base[v][1] += 1

        result = []
        for v in data_base:
            count = min(data_base[v][0], data_base[v][1])
            result.extend([v] * count)
        return result

        
    def intersect_2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map_1, map_2 = dict(), dict()
        for v in nums1:
            if v in map_1:
                map_1[v] += 1
            else:
                map_1[v] = 1
        for v in nums2:
            if v in map_2:
                map_2[v] += 1
            else:
                map_2[v] = 1
        result = list()
        for v in map_1:
            if v in map_2:
                count = min(map_1[v], map_2[v])
                result.extend([v] * count)
        return result

# @lc code=end

