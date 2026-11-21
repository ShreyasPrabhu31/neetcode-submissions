class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = 0
        count = 0
        map = {0 : 1}

        for n in nums:
            curSum += n
            if curSum - k in map:
                count += map[curSum - k]
            map[curSum] = 1 + map.get(curSum, 0)
        return count