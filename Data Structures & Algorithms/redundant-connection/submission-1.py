class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            p1, p2 = find(a), find(b)

            if p1 == p2:
                return False
            
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1

            parent[p2] = p1
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]
        
        return []