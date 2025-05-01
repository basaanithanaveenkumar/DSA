class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source==destination:
            return True 
        d=defaultdict(list)
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        seen_lst=set()
        seen_lst.add(source)

        def dfs(node):
            if node==destination:
                return True
            seen_lst.add(node)
            for negh in d[node]:
                if negh not in seen_lst:
                    seen_lst.add(negh)
                    if dfs(negh):
                        return True
            return False
        return  dfs(source)
        