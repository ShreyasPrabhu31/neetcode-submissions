class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minPrice = prices[0]

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxP:
                maxP = prices[i] - minPrice
        return maxP