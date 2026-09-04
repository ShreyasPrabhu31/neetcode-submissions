class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = defaultdict(int)
        best = 0

        for r in range(len(s)):
            count[s[r]] += 1
            while count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best