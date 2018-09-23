# https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def check(self,letters):
        for key in letters:
            if letters[key]<=0:
                continue
            else:
                return False
        return True
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters ={}
        for i in t:
            if i in letters:
                letters[i]+=1
            else:
                letters[i]=1
        start = 0
        output = s+"a"
        
        while start<len(s):
            if s[start] not in letters:
                start+=1
            else:
                break
        end = start
        
        while end<len(s):
            if s[end] not in letters:
                end+=1
                continue
            
            letters[s[end]]-=1
            while self.check(letters):
                if len(s[start:end+1]) < len(output):    
                    output = s[start:end+1]
                letters[s[start]]+=1
                start+=1
                while start<len(s) and s[start] not in letters:
                    start+=1
            end+=1 
            
        if len(output) < len(s)+1:
            return output
        else:
            return ""
                
