class StockSpanner:

    def __init__(self):
        self.input=[]        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if len(self.input)==0:
            self.input.append([price,1])
            return 1
        else:
            x , c = self.input[len(self.input)-1]
            if price<x:
                self.input.append([price,1])
                return 1
            else:
                count=1
                while price>=x :
                    count+=c
                    self.input.pop()
                    if len(self.input)>0:
                        x , c = self.input[len(self.input)-1]
                    else:
                        break
                self.input.append([price,count])
            return count
                        
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)