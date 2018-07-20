class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        map = {}
        count=0
        for i in wall:
            for j in i:
                count = count+j
                if count in map:
                    map[count]+=1
                else:
                    map[count]=1
            map[count]=0
            count=0
        max=0
        for i in map:
            if map[i]>max:
                max=map[i]
        return len(wall)-max
        