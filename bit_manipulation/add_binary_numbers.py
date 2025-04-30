class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a,b=int(a,2),int(b,2)

        while b: #until no carry
            without_carry= a^b
            with_carry = (a&b) <<1
            a,b=without_carry, with_carry
        return bin(a)[2:]
        