#https://leetcode.com/problems/max-consecutive-ones/
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        a = b = 0
        for num in nums:
            a = a + 1 if num == 1 else 0
            b = max(b, a)
        return b

