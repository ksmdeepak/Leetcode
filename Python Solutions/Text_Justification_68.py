#https://leetcode.com/problems/text-justification/description/

class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        output=[]
        temp=[]  
        count =0
        i=0    
        while i<len(words):
        
            if (len(words[i])+count+len(temp))<=maxWidth:
                count+=len(words[i])
                temp.append(words[i]+" ")
                i+=1
               
            else:
                temp[len(temp)-1] = temp[len(temp)-1][:-1]
                if len(temp)>1:
                    fillCount = maxWidth - len(temp) - count+1
                    j=0
                    while fillCount>0:
                        if j<len(temp)-1:
                            temp[j]+=" "
                            j+=1
                            fillCount-=1
                        else:
                            j=0
                else:
                    fillCount = maxWidth - len(temp[0])
                    temp[0]+=" "*fillCount
                       

                output.append(''.join(temp))
                temp=[]
                count=0
                
            
                
        if len(temp)!=0:
            temp[len(temp)-1] = temp[len(temp)-1][:-1]
            output.append(''.join(temp))
            
        temp = output.pop().split(" ")
        lastLine = ""
        for i in temp:
            lastLine+=i+" "
        lastLine = lastLine[:-1]
        l = len(lastLine)
        for i in range(l,maxWidth):
            lastLine+=" "
        output.append(lastLine)
        return output
        
