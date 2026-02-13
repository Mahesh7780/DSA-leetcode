#https://leetcode.com/problems/max-consecutive-ones/
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        a = b = 0
        for num in nums:
            a = a + 1 if num == 1 else 0
            b = max(b, a)
        return b

#or
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        count = 0
        
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
                
        return max_count


