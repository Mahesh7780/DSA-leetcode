#https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        d = nums1 + nums2
        c = sorted(d)
        n = len(c)

        if n % 2 == 1:
            return c[n // 2]
        else:
            return (c[n // 2 - 1] + c[n // 2]) / 2.0
            
# import numpy as np
        # c=nums1+nums2
        # d=sorted(c)
        # m=np.median(d)
        # return m
