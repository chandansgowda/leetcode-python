# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        c = 1
        left,right=None,None
        n = 0
        while temp:
            if n==k-1:
                left = temp
            temp=temp.next
            n+=1
        temp = head
        while temp:
            if c==n-k+1:
                right = temp
            temp = temp.next
            c+=1
        left.val,right.val=right.val,left.val
        return head
