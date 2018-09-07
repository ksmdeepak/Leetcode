class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = [int(v) for v in version1.split('.')]
        version2 = [int(v) for v in version2.split('.')]
        l1 = len(version1)
        l2 = len(version2) 
        l = l1 if l1>l2 else l2
        
        for i in range(0,l):
            v1 = version1[i] if i<l1 else 0
            v2 = version2[i] if i<l2 else 0
            if v1==v2:
                continue
            elif v1>v2:
                return 1
            else:
                return -1
            
        
        return 0