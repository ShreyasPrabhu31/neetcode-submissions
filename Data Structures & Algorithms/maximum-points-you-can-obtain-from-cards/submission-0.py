class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0
        curSum = 0
        maxSum = float('-inf')
        total = sum(cardPoints)

        if k == len(cardPoints):
            return total
        
        for r in range(len(cardPoints)):
            curSum += cardPoints[r]
            if r - l + 1 == len(cardPoints) - k:
                maxSum = max(maxSum, total - curSum)
                curSum -= cardPoints[l]
                l += 1
        return maxSum