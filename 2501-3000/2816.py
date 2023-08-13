# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            temp = head
            prev = None
            while temp:
                x = temp.next
                temp.next = prev
                prev = temp
                temp = x
            return prev
        
        head = reverse(head)
        
        temp = head
        carry = 0
        while temp:
            curVal = (temp.val*2)+carry
            temp.val = curVal%10
            carry = curVal//10
            temp = temp.next 
        
        head = reverse(head)
        
        if carry>0:
            temp = ListNode(carry)
            temp.next = head
            return temp
        
        return head
