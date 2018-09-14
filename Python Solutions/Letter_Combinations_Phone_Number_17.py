
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        output = set()
        keyMap ={}
        keyMap['2'] =['a','b','c'] 
        keyMap['3'] =['d','e','f'] 
        keyMap['4'] =['g','h','i'] 
        keyMap['5'] =['j','k','l'] 
        keyMap['6'] =['m','n','o'] 
        keyMap['7'] =['p','q','r','s'] 
        keyMap['8'] =['t','u','v'] 
        keyMap['9'] =['w','x','y','z']
        
        for i in digits:
            if len(output)==0:
                for y in keyMap[i]:
                    output.add(y)
            else:
                temp=[]
                for x in output:
                    temp.append(x)
                output=set()
                for x in temp:
                    for y in keyMap[i]:
                        output.add(x+y)
        return list(output)