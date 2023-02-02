class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        return "".join([x for (_,x) in sorted(zip(indices,s))])
        
        
 class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        l =  [0 for _ in range(len(s))]

        for i in range(len(indices)):
            l[indices[i]]=s[i]

        return "".join(l)
