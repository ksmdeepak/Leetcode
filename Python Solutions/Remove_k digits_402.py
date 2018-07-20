class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
       
        num = list(num)
        i=0
        while(i<len(num)):
            if k==0:
                break
            if i+1+k >len(num):
                del num[i]
                i=i-1
                k=k-1
            else:
                x = num[i+1:i+1+k]
                for item in x:     
                    if num[i]>item:
                        del num[i]
                        i=i-1
                        k=k-1 
                        break
            i+=1
        
        if len(num)!=0:
            if num[0]=='0':
                while(len(num) >0 and num[0]=='0'):
                    del num[0]
        if len(num)==0:
            num="0"
        return ''.join(num)