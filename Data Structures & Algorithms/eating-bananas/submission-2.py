class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_taken(rate):
            # Comments added line by line
            time = 0
            for i in range(len(piles)):
                # Ceiling division gives hours needed for pile i at this rate
                time += (piles[i] + rate - 1) // rate
            return time

        l, r = 1, max(piles)  # Search range: slowest possible to fastest useful rate

        while l < r:
            mid = (l + r) // 2  # Candidate harvest rate

            if time_taken(mid) > h:
                # Too slow — this rate doesn't finish in time, need a faster rate
                l = mid + 1
            else:
                # Fast enough — this rate works, but a slower rate might also work
                # Keep mid in the search range since it's a valid candidate
                r = mid

        return l  # l == r at this point, the minimum valid rate