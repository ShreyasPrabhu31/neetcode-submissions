class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            #If target is found return the index
            if nums[m] == target:
                return m
            
            #If the left part of the array is sorted
            if nums[l] <= nums[m]:
                #If target isn't present in the left sorted half
                if target < nums[l] or target > nums[m]:
                    l = m + 1#Search right half
                else:
                    r = m - 1#Search left half
            #If right part of the array is sorted
            else:
                #If target isn't present in the right sorted half
                if target > nums[r] or target < nums[m]:
                    r = m - 1#Search left half
                else:
                    l = m + 1#Search right half
        #If we couldn't find the target return -1
        return -1