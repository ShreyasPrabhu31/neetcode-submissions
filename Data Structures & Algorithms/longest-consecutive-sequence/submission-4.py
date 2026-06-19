class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        unqNums = set(nums)

        for n in unqNums:
            if n - 1 not in unqNums:
                nxtNum = n + 1
                length = 1
                while nxtNum in unqNums:
                    nxtNum += 1
                    length += 1
                res = max(res, length)
        return res