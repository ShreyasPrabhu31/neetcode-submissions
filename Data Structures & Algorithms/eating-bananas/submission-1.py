class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_taken(rate):
            time = 0
            for i in range(len(piles)):
                time += (piles[i] + rate - 1) // rate
            return time
        
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if time_taken(mid) > h:
                l = mid + 1
            else:
                r = mid
        return l