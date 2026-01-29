#https://leetcode.com/problems/categorize-box-according-to-criteria/description/
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:


            volume = length * width * height
            bulky = (length >= 10**4 or width >= 10**4 or height >= 10**4 or volume >= 10**9)
            heavy = (mass >= 100)
            if bulky and heavy:
                return "Both"
            elif not bulky and not heavy:
                return "Neither"
            elif  bulky:
                return "Bulky"
            else:
                return "Heavy"
