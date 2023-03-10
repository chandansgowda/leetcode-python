# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        count = 0
        while temp:
            temp=temp.next
            count+=1
        temp = head
        count-=1
        val = 0
        while count>=0:
            if temp.val==1:
                val += (2**count)
            count-=1
            temp=temp.next
        return val
