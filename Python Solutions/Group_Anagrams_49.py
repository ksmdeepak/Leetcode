class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        temp=[]
        for i in strs:        
            temp.append(''.join(sorted(i)))
        hashMap = {}
        for i in range(len(temp)):
            if temp[i] not in hashMap:
                hashMap[temp[i]]=[]
            hashMap[temp[i]].append(strs[i])
        output=[]
        for item in hashMap:
            output.append(hashMap[item])
        return output
                
        