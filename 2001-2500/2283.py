class Solution:
    def digitCount(self, num: str) -> bool:
        d = {}
        for i in range(len(num)):
            d[str(i)] = 0
        
        for i in range(len(num)):
            if num[i] in d:
                d[num[i]]+=1
        
        for i in range(len(num)):
            if int(num[i])!= d[str(i)]:
                return False
        
        return True
