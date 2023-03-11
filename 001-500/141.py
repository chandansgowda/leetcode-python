# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            s = head
            f = s.next

            while s is not f:
                s = s.next
                f = f.next.next

            return True
        except:
            return False

        
        
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: 
            return False
        s = head
        f = head.next

        if s==f:
                return True

        while s is not f and f and f.next and f.next.next:
            s = s.next
            f = f.next.next
            if s==f:
                return True

        return False

        
