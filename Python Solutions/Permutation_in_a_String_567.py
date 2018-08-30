class Solution(object):
    def compare(self,x,y):
        if(len(x)!=len(y)):
            return False
        else:
            for i in x:
                if i not in y:
                    return False
                elif x[i]!=y[i]:
                    return False
        return True
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if(len(s1)>len(s2)):
            return False
        map1={}
        map2={}
        for i in s1:
            if i not in map1:
                map1[i]=1
            else:
                map1[i]+=1
        window=len(s1)
        for i in range(window):
            if s2[i] not in map2:
                map2[s2[i]]=1
            else:
                map2[s2[i]]+=1
        left=0
        right=window-1
        if(self.compare(map1,map2)):
            return True
        else:
            while self.compare(map1,map2)==False:
                if right+1<len(s2):
                    right+=1
                    if s2[right] not in map2:
                        map2[s2[right]]=1
                    else:
                        map2[s2[right]]+=1
                    if map2[s2[left]]>1:
                        map2[s2[left]]-=1
                    else:
                        del map2[s2[left]]
                    left+=1
                else:
                    return False
        return True
        