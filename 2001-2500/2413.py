class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n
        return n*2
    
    
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n << (n & 1)
    
 
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n*2 if n%2!=0 else n
