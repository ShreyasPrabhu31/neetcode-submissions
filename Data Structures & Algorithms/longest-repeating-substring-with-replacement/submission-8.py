class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = defaultdict(int)
        maxf = 0
        best = 0

        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best