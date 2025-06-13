class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        #power=[]
        powerset=[]
        power_set=1<<n
        for i in range(power_set):
            power=[]
            for j in range(n):
                if (i>>j)&1:
                    power.append(nums[j])
            powerset.append(power)
        return powerset