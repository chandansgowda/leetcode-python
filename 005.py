# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = t = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1 = l1.next
            if l2:
                carry+=l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            t.next = ListNode(val)
            t = t.next

        return head.next
