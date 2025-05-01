class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g=defaultdict(list)
        courses=prerequisites
        for u,v in courses:
            g[u].append(v)
        unseen=0
        visiting=1
        visited=2
        states=[unseen]*numCourses

        def dfs(node):
            state=states[node]
            if state==visited: return True
            elif state==visiting: return False
            states[node]=visiting

            for n in g[node]:
                if not dfs(n):
                    return False
            states[node]=visited
            return True
            


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True    
        