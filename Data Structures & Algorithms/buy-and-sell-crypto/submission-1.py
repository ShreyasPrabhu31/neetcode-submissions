class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = float("-inf")
        minPrice = max(prices)

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            if prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        return maxProfit