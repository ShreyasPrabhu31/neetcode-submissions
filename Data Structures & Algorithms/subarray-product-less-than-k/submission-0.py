class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        product = 1

        if k <= 1:
            return 0

        for r in range(len(nums)):
            product *= nums[r]
            while product >= k:
                product /= nums[l]
                l += 1
            count += r - l + 1
        return count