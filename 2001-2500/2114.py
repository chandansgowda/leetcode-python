class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        mx = 0
        for sentence in sentences:
            nw = len(sentence.split())
            if nw>mx:
                mx = nw

        return mx
    
    
    
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        m = 0
        for sentence in sentences:
            m = max(m,sentence.count(" ")+1)

        return m
