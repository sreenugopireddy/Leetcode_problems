# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        n = 0
        temp = head
        while temp:
            n  = n + 1
            temp = temp.next
        m = n // 2
        temp = head
        for i in range(m):
            temp = temp.next
        return temp