class Solution(object):
    def removeDuplicates(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast = slow = count = 0
        while fast<len(arr):
            if arr[fast]==arr[slow]:
                fast+=1
            else:
                count+=1
                slow+=1
                arr[slow]=arr[fast]
                fast+=1

        return count+1
