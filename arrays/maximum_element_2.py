# my own solution 
#time complexity o(2N)


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        d_numb={}
        for numb in nums:
            if numb not in d_numb:
                d_numb[numb]=1
            else:
                d_numb[numb]+=1
        for keys,values in d_numb.items():
            if values>(len(nums)//3):
                ans.append(keys)
        return ans