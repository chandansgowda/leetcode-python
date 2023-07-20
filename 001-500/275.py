class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l,h=0,len(citations)-1
        while l<=h:
            m = (l+h)>>1
            if citations[m]==len(citations)-m:
                return len(citations)-m
            elif citations[m]<len(citations)-m:
                l = m+1
            else:
                h = m-1
        return len(citations)-l
                
