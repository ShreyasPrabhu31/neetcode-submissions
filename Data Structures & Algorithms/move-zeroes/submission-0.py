class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nxtNonZero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nxtNonZero], nums[i] = nums[i], nums[nxtNonZero]
                nxtNonZero += 1
                