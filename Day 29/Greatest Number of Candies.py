#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        r=[]
        for i in candies:
            r.append(i+extraCandies>=max(candies))
        return r
