#https://leetcode.com/problems/find-the-difference/description/
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a=sorted(t)
        b=sorted(s)
        for i in range (len(b)):
            if b[i]!=a[i]:
                return a[i]
        return a[-1]
