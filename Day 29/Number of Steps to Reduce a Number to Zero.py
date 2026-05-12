#https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
class Solution:
    def numberOfSteps(self, num: int) -> int:
        s=0
        while num:
            num=num//2 if num%2==0 else num -1
            s+=1
        return s
        
