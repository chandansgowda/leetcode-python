# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)

        dummy = ListNode(next=head)
        prev = dummy
        cur = dummy.next

        while cur:
            midNode = ListNode(val=math.gcd(prev.val,cur.val), next=prev.next)
            prev.next = midNode
            prev = cur
            cur = cur.next
        
        return dummy.next.next


        
