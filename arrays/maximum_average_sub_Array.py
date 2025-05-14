class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        lp=0
        rp=k
        max_avg=0
        for i in range(len(nums)-k):
            #print(nums[lp:rp])
            max_avg=max(sum(nums[lp:rp])/k,max_avg)
            lp+=1
            rp+=1
        return max_avg
#time complexity o(n)