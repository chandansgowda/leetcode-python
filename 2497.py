class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        m = 0

        for x in strs:
            if x.isdigit():
                if int(x)>m:
                    m = int(x)

            elif x.isalpha():
                if len(x)>m:
                    m=len(x)

            else:
                if len(x)>m:
                    m=len(x)

        return m
