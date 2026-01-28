#https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums):
        # nums.sort()
        # return nums[len(nums)//2]

        #or
        return max(set(nums), key=nums.count)
