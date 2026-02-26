#https://leetcode.com/problems/add-digits/description/
class Solution:
    def addDigits(self, num: int) -> int:
         while num >= 10:
             s = 0
             t = num 
             while t > 0:
                 s += t % 10
                 t //= 10
                 num= s
        return(num)
# OR
        while num >=10:
    
            b= [int(d) for d in str(num)]
            num=sum(b)
        return num
