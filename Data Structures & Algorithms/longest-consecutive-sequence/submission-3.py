class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        uniqNums = set(nums)

        for n in uniqNums:
            if n - 1 not in uniqNums:
                nxtNum = n + 1
                length = 1
                while nxtNum in uniqNums:
                    nxtNum += 1
                    length += 1
                res = max(res, length)
        return res