'''
Delete Columns to Make Sorted
'''

class Solution(object):
    def minDeletionSize(self, arr):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        for i in range(len(arr[0])):
            j = 0
            while j<len(arr)-1:
                if arr[j][i] > arr[j+1][i]:
                    count+=1
                    break
                j+=1
        return count
