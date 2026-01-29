#https://leetcode.com/problems/remove-zeros-in-decimal-representation/description/
class Solution:
    def removeZeros(self, n: int) -> int:

        j = list(str(n))

        while '0' in j:
            j.remove('0')

        return int(''.join(j))
