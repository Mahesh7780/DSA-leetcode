#https://leetcode.com/problems/length-of-last-word/description/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        m=s.split() # i split the sentence
        l=len(m[-1]) # storing the length of last word in the sentence
        return l
        
        #or
        return (len(m[-1]))
