class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest=nums[0]
        for n in nums:
            if abs(n)<abs(closest):
                closest=n
        if closest<0 and abs(closest) in nums:
            # in forms a another loop
            return abs(closest)
        else:
            return closest
        #time compleity =O(2n) = O(n)
        # space complexity = O(1)