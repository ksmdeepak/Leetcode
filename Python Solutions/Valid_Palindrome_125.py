class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s)==0:
            return True
        l = 0
        r = len(s)-1
        while(l<r and l<len(s) and r>=0):
           
            while l<len(s) and (s[l]==" " or not s[l].isalnum()) :
                l+=1
            while r>=0 and (s[r]==" " or not s[r].isalnum()):
                r-=1
            if(l<r):
                if s[l].lower()==s[r].lower():
                    l+=1
                    r-=1
                else:
                    return False
        return True