class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        arr = []
        arr.append(first)

        for e in encoded:
            first ^= e
            arr.append(first)

        return arr
