#https://leetcode.com/problems/detect-capital/submissions/2001054811/
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower() or word.istitle():
            return True
        return False
