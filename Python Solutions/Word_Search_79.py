class Solution(object):
    def search(self,board,visited,word,index,i,j,m,n):
        
        if board[i][j]!=word[index]:
            return False
        if not visited[i][j] and board[i][j]==word[index] and index==len(word)-1:
            return True
        if not visited[i][j] and board[i][j]==word[index]:
            visited[i][j]=1
            
            a=b=c=d = False
            if i+1<m:
                a = self.search(board,visited,word,index+1,i+1,j,m,n)   
            if a:
                return a
            if i-1 >=0 :
                b = self.search(board,visited,word,index+1,i-1,j,m,n)  
            if b:
                return b
            if j+1<n:
                c = self.search(board,visited,word,index+1,i,j+1,m,n)  
            if c:
                return c
            if j-1>=0 :
                d = self.search(board,visited,word,index+1,i,j-1,m,n) 
            if d:
                return d
            visited[i][j]=0
            return False
        return False
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        found = False
        visited = [[0 for x in range(n)] for y in range(m)] 
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    found = self.search(board,visited,word,0,i,j,m,n)
                    if found:
                        return found
                    visited = [[0 for x in range(n)] for y in range(m)] 
        return found