# new solution by me for hamming weight

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod_out=0
        div_out=0
        count=0
        while n!=0:
            if n%2==1:
                count+=1
            n=n//2
        return count             
