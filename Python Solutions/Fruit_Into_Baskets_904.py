# https://leetcode.com/problems/fruit-into-baskets/description/

class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        stack={}
        stack[tree[0]] = 1
        total =1
        mx = 1
        prev = tree[0]
        for i in range(1,len(tree)):
            if tree[i]==prev:
                total+=1
                stack[prev]+=1
                if total>mx:
                    mx=total
            elif tree[i] in stack:
                total+=1
                prev = tree[i]
                stack[prev]=1
                if total>mx:
                    mx=total
            elif len(stack)==1:
                total+=1
                prev = tree[i]
                stack[prev]=1
                if total>mx:
                    mx=total
            else:
                total = stack[prev]
                total+=1
                temp = None
                for key in stack:
                    if key!=prev:
                        temp=key
                stack.pop(temp)
                prev=tree[i]
                stack[prev]=1
                if total>mx:
                    mx = total
        return mx
                
                
                
                    
