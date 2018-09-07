class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        output = []
        flag=0
        while n>0:
            temp = n%26
            if temp==0:
                temp=26
                flag=1
            output = [chr(temp +64)] + output
            n = n//26
            if flag:
                n-=1
                flag=0
        return ''.join(output)
            