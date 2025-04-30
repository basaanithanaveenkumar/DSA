class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        org_num=num
        num=(abs(num))
        rem=[]
        while num>0:
            rem.append(str(num%7))
            num//=7
        if org_num<0:
            rem.append("-")
        rem.reverse()
        return "".join(rem)


        