#https://leetcode.com/problems/count-operations-to-obtain-zero/?envType=daily-question&envId=2026-02-01
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0

        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
            count += 1

        return count
        
#or

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0

        while num1 and num2:
            if num1 >= num2:
                count += num1 // num2
                num1 %= num2
            else:
                count += num2 // num1
                num2 %= num1

        return count

