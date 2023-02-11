class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0 for _ in range(n)]

        l,h=0,n-1
        while l<h:
            res[l],res[h]=-h,h
            l+=1
            h-=1

        return res
      
 class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        a = range(1,n)
        return a + [-sum(a)]
