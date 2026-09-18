class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedSum = (len(nums) * (len(nums) + 1)) // 2
        actualSum = 0

        for n in nums:
            actualSum += n
        return expectedSum - actualSum