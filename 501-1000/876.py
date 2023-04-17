# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count=0
        while temp:
            temp=temp.next
            count+=1
        count//=2
        temp = head
        while count!=0:
            temp=temp.next
            count-=1
        return temp
