# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = head.next
        c = 0
        while p2:
            if p2.val==0:
                p1 = p1.next
                p1.val = c
                c = 0
            else:
                c+=p2.val
            p2 = p2.next
        p1.next = None
        return head.next
        


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        res = []
        while temp:
            c = 0
            while temp.val!=0:
                c += temp.val
                temp = temp.next
            if c!=0:
                res.append(c)
            temp = temp.next
        
        z = ListNode(res[0])
        x = z
        for i in res[1:]:
            x.next = ListNode()
            x = x.next
            x.val = i
            

        return z
