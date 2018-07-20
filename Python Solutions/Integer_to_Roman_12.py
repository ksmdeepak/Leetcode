class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        output=""
        list=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        map={}
        map[1000]='M'
        map[900]='CM'
        map[500]='D'
        map[400]='CD'
        map[100]='C'
        map[90]='XC'
        map[50]='L'
        map[40]='XL'
        map[10]='X'
        map[9]='IX'
        map[5]='V'
        map[4]='IV'
        map[1]='I'
        
        for i in range(0,len(list)):
            value = int(num/list[i])
            while value>0:
                output=output+map[list[i]]
                value-=1
            num=num%list[i]
       
        return output
            