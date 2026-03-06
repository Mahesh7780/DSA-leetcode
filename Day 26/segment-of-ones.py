#https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/?envType=daily-question&envId=2026-03-06
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        a = False
        for c in s:
            if c == '0':
                a = True
            elif a:
                return False

        return True
