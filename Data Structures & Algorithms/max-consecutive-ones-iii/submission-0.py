class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        countZero = 0
        n = len(nums)

        for r in range(n):
            if nums[r] == 0:
                countZero += 1
            if countZero > k:
                if nums[l] == 0:
                    countZero -= 1
                l += 1
        return n - l    