#https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n):
        # if n<=2:
        #     return n
        # else : return (n-1)+(n-2)  #using recorsion
        
        
        
        # or
        
        
        a,b=0,1
        if n<=2:
            return n
        else:    
            for i in range(n):
                a,b=b,a+b
            return b
            
