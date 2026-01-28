#https://leetcode.com/problems/contains-duplicate/submissions/1899701213

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=set()
        for i in nums:  # [1,1,1,3,3,4,3,2,4,2]
            if i in a:  #    
                return True 
            a.add(i) # 1 , 2,3,1
        return False
        
        
        # OR
        
        dic={}
        
        for i in nums:
            dic[i] = dic.get(i,0) + 1  # { 1: 2, 2: 1, 3: 1} 
            
        for j in dic.values():
            if j>=2:
                return True
        else : 
            return False
        
        
