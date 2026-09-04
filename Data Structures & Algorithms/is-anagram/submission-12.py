class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charS, charT = {}, {}

        for c in s:
            if c not in charS:
                charS[c] = 1
            charS[c] += 1
        
        for c in t:
            if c not in charT:
                charT[c] = 1
            charT[c] += 1
        
        return charS == charT