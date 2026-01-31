#https://leetcode.com/problems/sort-vowels-in-a-string/?envType=daily-question&envId=2026-01-31

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        
        v = []
        for ch in s:
            if ch in vowels:
                v.append(ch)  
        
        v.sort()
        result = "" 
        i = 0 
        for ch in s:
            if ch in vowels:
                result += v[i] 
                i += 1
            else:
                result += ch
        
        return result
