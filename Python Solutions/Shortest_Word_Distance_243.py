# https://leetcode.com/problems/shortest-word-distance/description/

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        wordMap = {}
        for i in range(len(words)):
            if words[i] not in wordMap:
                wordMap[words[i]]=[]
            wordMap[words[i]].append(i)
        a = wordMap[word1]
        b = wordMap[word2]
        mn = len(words)
        i=j=0
        while i<len(a) and j<len(b):
            mn = min(mn,abs(a[i]-b[j]))
            if a[i]>b[j]:
                j+=1
            else:
                i+=1
        return mn
        
