class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count={}
        status={}
        for i in s:
            if i not in count:
                count[i]=1
                status[i]=False
            else:
                count[i]+=1
        stack =[]
        i=0
        while i<len(s):
            
            if len(stack)==0:
                stack.append(s[i])
                status[s[i]]=True
                
            else:
                if stack[len(stack)-1]< s[i] and status[s[i]]==False:
                    stack.append(s[i])
                    status[s[i]]=True
                elif stack[len(stack)-1] > s[i] and status[s[i]]==False:
                    if count[stack[len(stack)-1]]==0:
                       stack.append(s[i])
                       status[s[i]]=True
                    else:
                       x=stack.pop()
                       status[x]= False
                       i-=1
                       count[s[i]]+=1
                       
                        
            count[s[i]]-=1
            i+=1
        s=""
        for i in stack:
            s=s+i
        return s
            
        