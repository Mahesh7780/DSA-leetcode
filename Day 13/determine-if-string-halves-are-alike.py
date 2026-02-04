#https://leetcode.com/problems/determine-if-string-halves-are-alike/description/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        m=len(s)//2
        l1=s[:m]
        l2=s[m:]
        a=0
        b=0
        v = "aeiouAEIOU"
        for char in l1:
            if char in v:
                a+=1
        for char in l2:
            if char in v:
                b+=1
        if a==b:
            return True
        return False
