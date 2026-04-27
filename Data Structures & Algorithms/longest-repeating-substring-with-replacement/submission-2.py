class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # #This works but is slow because it checks many overlapping substrings.
        # #Brute force: O(n^2), O(m) where n is the len of string and m is the number of unique chars in the string
        # res = 0

        # for i in range(len(s)):
        #     count, maxf = {}, 0
        #     for j in range(i, len(s)):
        #         count[s[j]] = 1 + count.get(s[j], 0)
        #         maxf = max(maxf, count[s[j]])
        #         if (j - i + 1) - maxf <= k:
        #             res = max(res, j - i + 1)
        # return res

        l = 0
        res = 0
        count = {}
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res