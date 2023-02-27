#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

#The overall run time complexity should be O(log (m+n)).


#Approach 1
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        n = len(nums1)
        if n%2==0:
            return (nums1[n//2-1]+nums1[n//2])/2
        else:
            return nums1[n//2]


#Approach 2
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        i=j=0
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1+n2
        while i<n1 and j<n2:
            if nums1[i]<=nums2[j]:
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1
        while i<n1:
            arr.append(nums1[i])
            i+=1
        while j<n2:
            arr.append(nums2[j])
            j+=1
            
        if n%2==0:
            return (arr[int(n/2-1)]+arr[int(n/2)])/2
        else:
            return arr[n//2]
