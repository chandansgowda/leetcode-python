class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        m = 0
        x = 0
        for i in range(0, len(gain)):
            x += gain[i]
            m = max(m,x)

        return m
