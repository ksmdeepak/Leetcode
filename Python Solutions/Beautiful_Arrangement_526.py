class Solution:
    def __init__(self):
        
        self.status={}
        self.output=[]
        self.temp=[]
    def dfs(self,i,N):
        if(i>N):
            if self.temp not in self.output:
                self.output.append(self.temp)
                self.temp=[i for i in self.temp ]
            return
#    
        for j in range(1,N+1) :
            if (i%j==0 or j%i==0) and self.status[j]==0:
                self.status[j]=1
                self.temp[j-1]=i
                self.dfs(i+1,N)
                self.status[j]=0
           
               
                
           
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """   
       
           
        for i in range(1,N+1):
            self.status[i]=0
            self.temp.append(i)
        
        
        self.dfs(1,N)
       
        return len(self.output)
                