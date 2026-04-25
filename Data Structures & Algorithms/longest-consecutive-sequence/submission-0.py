class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for n in nums: #Iterate through all numbers in the i/p array
            if n - 1 not in s: #To check if n is the start of a sequence
                nxt_num = n + 1  
                length = 1
                while nxt_num in s: #Check if the next element is present
                    length += 1
                    nxt_num += 1
                longest = max(longest, length)
        return longest