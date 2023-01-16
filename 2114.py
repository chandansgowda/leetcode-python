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
