#https://leetcode.com/problems/maximum-gap/description/
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<2:
            return 0
        else:
            d= [nums[i + 1] - nums[i]for i in range(len(nums) - 1)]
            c=max(d)
        return c
