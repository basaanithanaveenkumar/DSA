class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letters={}
        for i in range(len(magazine)):
            if magazine[i] not in letters:
                letters[magazine[i]]=1
            else:
                letters[magazine[i]]+=1
        for i in range(len(ransomNote)):
            if ransomNote[i] not in letters:
                return False
            if letters[ransomNote[i]]==1:
                del letters[ransomNote[i]]
            if ransomNote[i] in letters:
                letters[ransomNote[i]]-=1
        return True
        