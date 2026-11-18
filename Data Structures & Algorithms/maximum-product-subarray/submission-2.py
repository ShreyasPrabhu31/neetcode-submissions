class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = float("-inf")
        prefix = 1
        postfix = 1
        n = len(nums)

        for i in range(n):
            if prefix == 0:
                prefix = 1
            if postfix == 0:
                postfix = 1
            
            prefix *= nums[i]
            postfix *= nums[n - i - 1]
            maxProd = max(maxProd, prefix, postfix)
        
        return maxProd