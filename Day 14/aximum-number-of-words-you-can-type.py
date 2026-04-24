#https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/?envType=daily-question&envId=2026-02-05

class Solution(object):
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        m = text.split()
        count = 0
        for i in m:
            for j in brokenLetters:
                if j in i:
                    break
            else:
                count += 1
        return count
        
#OR
        broken = set(brokenLetters)
        count = 0

        for word in text.split():
            if not any(ch in broken for ch in word):
                count += 1

        return count
