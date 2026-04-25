class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        if len(s) != len(t):
            return False
        
        for c in s:
            if c not in countS:
                countS[c] = 1
            else:
                countS[c] += 1
        
        for c in t:
            if c not in countT:
                countT[c] = 1
            else:
                countT[c] += 1
        
        return countS == countT