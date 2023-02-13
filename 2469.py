class Solution(object):
    def convertTemperature(self, c):
        """
        :type celsius: float
        :rtype: List[float]
        """
        return [c+273.15, c*1.8+32]
