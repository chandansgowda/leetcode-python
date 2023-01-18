class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = (high+low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1

        return low
