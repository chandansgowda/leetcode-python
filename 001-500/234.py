# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        return arr == arr[::-1]
