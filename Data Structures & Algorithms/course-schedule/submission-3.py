class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for crs, pre in prerequisites:
            g[crs].append(pre)
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if g[crs] == []:
                return True
            
            visit.add(crs)
            for pre in g[crs]:
                if not dfs(pre):
                    return False
            
            visit.remove(crs)
            g[crs] = []
            return True
        

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True