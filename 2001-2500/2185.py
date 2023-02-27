class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        pl = len(pref)
        for word in words:
            if word.startswith(pref):
                count+=1

        return count
