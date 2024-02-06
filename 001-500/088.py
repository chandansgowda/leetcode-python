class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m+n-1
        i = m-1
        j = n-1

        while j>=0:
            if i>=0 and nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
                k-=1
            else:
                nums1[k]=nums2[j]
                j-=1
                k-=1
                


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m+n-1
        j = n-1
        k = m-1

        while j>=0 and k>=0:
            if nums2[j] > nums1[k]:
                nums1[i]=nums2[j]
                j-=1
            else:
                nums1[i]=nums1[k]
                k-=1
            i-=1

        while i>=0 and j>=0:
            nums1[i]=nums2[j]
            j-=1
            i-=1
