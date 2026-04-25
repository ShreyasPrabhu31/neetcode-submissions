class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def unique(start, end):
            seen = set()
            
            for i in range(start, end):
                if s[i] in seen:
                    return False
                seen.add(s[i])
            return True
        
        n = len(s)
        res = 0

        for i in range(n):
            for j in range(i + 1, n + 1):
                if unique(i, j):
                    res = max(res, j - i)
        return res