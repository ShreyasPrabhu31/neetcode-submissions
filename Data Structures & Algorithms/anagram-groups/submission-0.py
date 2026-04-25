class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)     #Hashmap to store the counts as key and the list of anagrams as values.
        for s in strs:
            count = [0] * 26    # To count a - z
            for c in s:
                count[ord(c) - ord("a")] += 1   
            res[tuple(count)].append(s)     #Using a tuple as list cannot be keys in python.
        return res.values()