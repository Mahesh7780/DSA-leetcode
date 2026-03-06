#https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/description/

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max1 = max0 = 0
        cur1 = cur0 = 0
        for c in s:
            if c == '1':
                cur1 += 1
                cur0 = 0
            else:
                cur0 += 1
                cur1 = 0
            max1 = max(max1, cur1)
            max0 = max(max0, cur0)
        return max1 > max0



#this is my version wic work some test cases 
# class Solution:
#     def checkZeroOnes(self, s: str) -> bool:
#         a=""
#         b=""
#         d=False
#         for c in s:
#             if c=="1":
#                 a+=c
#             else:
#                 b+=c
#         if len(a)>len(b):
#             d= True
#         return d
        
