class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lp=0
        charset=set()
        res=0
        for rp in range(len(s)):
            if s[rp] in charset:
                charset.remove(s[lp])
                lp=+1
            charset.add(s[rp])
            
            res=max(res,lp-rp+1)
        return res
#time complexity : even though we have while  the time complexity is O(n)
