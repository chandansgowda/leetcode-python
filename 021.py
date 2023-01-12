# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, a, b):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = temp = ListNode()
        while a and b:
            if a.val<b.val:
                temp.next = a
                a = a.next
            else:
                temp.next = b
                b = b.next
            temp = temp.next
        temp.next = a or b
        return dummy.next
