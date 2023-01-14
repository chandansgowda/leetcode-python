class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = []
        small = float("inf")
        d = {}

        for i in range(len(list1)):
            if list1[i] in list2:
                d[list1[i]] = i
        
        for i in range(len(list2)):
            if list2[i] in d.keys():
                d[list2[i]]+=i
                if d[list2[i]]<small:
                    small = d[list2[i]]

        for k,v in d.items():
            if v==small:
                res.append(k)

        return res
