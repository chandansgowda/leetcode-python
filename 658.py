# Efficient
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr)-k
        while left < right:
            mid = (left+right)//2
            if x-arr[mid] > arr[mid+k] - x: 
                left = mid+1   # search right side
            else: right = mid  # search left side
        return arr[left:left+k]
      
# Easy
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = []
        for num in arr:
            l.append((abs(num-x), num))
        l.sort()
        return sorted([i[1] for i in l[:k]])
