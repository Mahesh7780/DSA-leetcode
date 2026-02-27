#https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x):

        if x < 0:
            d = -int(str(-x)[::-1])
        else:
            d = int(str(x)[::-1])
        if d < -2**31 or d > 2**31 - 1:
            d = 0
        return d
