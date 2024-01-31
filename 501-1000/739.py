class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0]*len(T) 
        stack = []
        
        for i,v in enumerate(T):
            while stack and stack[-1][1] < v:
                index,value = stack.pop()
                ans[index] = i - index
            stack.append([i,v])      
        
        return ans
