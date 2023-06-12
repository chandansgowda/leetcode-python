class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(arr, l, r):
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
    
        x = len(nums)-(k%len(nums))
        rev(nums, 0, x-1)
        rev(nums, x, len(nums)-1)
        rev(nums, 0, len(nums)-1)
