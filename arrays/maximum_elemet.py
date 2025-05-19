# solved on my own
#space=o(N) # hashset
# time=o(2N) =O(N)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_can=-1
        count=0
        dict_n={}
        for numb in nums:
            if numb not in dict_n:
                dict_n[numb]=1
            else:
                dict_n[numb]+=1
        for keys,values in dict_n.items():
            if values>count:
                count=values
                curr_can=keys
        return curr_can

        