class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        maxProd = float("-inf")
        n = len(nums)

        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            
            prefix *= nums[i]
            suffix *= nums[n - i - 1]
            maxProd = max(maxProd, prefix, suffix)
        return maxProd