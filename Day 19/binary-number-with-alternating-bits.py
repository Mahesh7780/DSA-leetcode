#https://leetcode.com/problems/binary-number-with-alternating-bits/description/
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b=bin(n)
        s=str(b)
        t=s[2:]
        for i in range (len(t)-1):
            if t[i]==t[i+1]:
                return False
        return True
        
        
