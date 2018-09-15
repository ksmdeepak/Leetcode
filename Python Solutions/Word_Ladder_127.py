# https://leetcode.com/problems/word-ladder/description/

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        queue=[(beginWord,1)]
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        while len(queue)>0:     
            temp,count = queue.pop(0)
            for i in range(len(temp)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = temp[0:i] + j + temp[i + 1:]
                    if new_word==endWord:
                        return count+1
                    elif new_word in wordList:
                        queue.append((new_word,count+1))
                        wordList.remove(new_word)
        return 0
