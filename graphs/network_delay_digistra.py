class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        g=defaultdict(list)
        for u,v,time in times:
            g[u].append((v,time))
        min_t={}
        min_heap=[(0,k)]  # source node

        while min_heap:
            time_i_k ,i=heapq.heappop(min_heap)
            if i in min_t:
                continue
            min_t[i]= time_i_k
            for nei,nei_t in g[i]:
                if nei not in min_t:
                    heapq.heappush(min_heap,(time_i_k+nei_t,nei))
        if len(min_t)==n:
            return max(min_t.values())
        else:
            return -1
