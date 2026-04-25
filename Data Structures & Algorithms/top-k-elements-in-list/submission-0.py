class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}      #Hash map to keep count of the values from i/p array
        freq = [[] for i in range(len(nums) + 1)]      #Array which is the same size as the input array whose index will be the freq(count) and the values will be the list of values that occurred a particular no of times.
        #To count no of times each value in nums occurres
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        #To get the key value pair in the dictionary count
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):   # To iterate backwards to get top k frequent elements
            for n in freq[i]:
                res.append(n)
                if len(res) == k:    #Break when the length of the res arr is same as k
                    return res
        