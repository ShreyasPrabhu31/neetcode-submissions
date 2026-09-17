class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        
        for u, v, w in times:
            adj[u].append((v, w))
        
        time = {}
        minHeap = [(0, k)]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in time:
                continue
            time[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in time:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        return max(time.values()) if len(time) == n else -1