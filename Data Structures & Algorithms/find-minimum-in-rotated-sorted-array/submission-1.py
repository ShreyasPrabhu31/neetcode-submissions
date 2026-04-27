class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
            
            m = (l + r) // 2
            #Min can be found at the mid index as well, so we check this
            res = min(res, nums[m])
            #Left half is sorted
            if nums[m] >= nums[l]:
                l = m + 1#Search in the right half
            #Right half is sorted
            else:
                r = m - 1#Search in the left half
        return res

