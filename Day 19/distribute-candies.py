# https://leetcode.com/problems/distribute-candies/description/
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)   #lenof candy
        m=len(set(candyType)) # candy to set
        a=len(candyType)//2 #len//2
        if m>a: #set len > a
            return a
        return m
#OR
        return min(len(set(candyType)),len(candyType)//2)

        
