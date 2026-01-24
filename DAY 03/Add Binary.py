#https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a,b):
        return bin(int(a, 2) + int(b, 2))[2:]
          # OR
        
#         c=int(a,2)
#         g=int(b,2)     
#         h=c+g
#         d=bin(h)
#         s=str(d)[2:]
#         return s 
        
        
        #OR
  
# # class Solution:
# #     def addBinary(self, a,b): 
# #         d= int(a,2)
# #         f= int (b,2)
# #         g= d+f
# #         return bin(g)[2:]
        
            
