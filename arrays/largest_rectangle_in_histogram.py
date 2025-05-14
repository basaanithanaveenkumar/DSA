# my solution O(N)
# but the test cases failes in the leet code

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        lp=0
        hp=0
        area=0
        if len(heights)==1:
            return heights[0]
        for index in range(len(heights)-1):
            lp=heights[index]
            rp=heights[index+1]
            minlr=min(lp,rp)
            area=max(2*minlr,area)
        return area

# right answer find the next samller and previous smaler