class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l_w=r_w=0
        n=len(height)
        max_l=[0]*n
        max_r=[0]*n

        for i in range(n):
            j=-i-1
            max_l[i]=l_w
            max_r[j]=r_w
            l_w=max(l_w,height[i])
            r_w=max(r_w,height[j])
        summ=0
        for i in range(n):
            pot=min(max_l[i],max_r[i])
            summ+=max(0,pot-height[i])   
        return summ