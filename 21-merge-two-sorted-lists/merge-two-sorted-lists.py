# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        temp1 = list1
        temp2 = list2
        dummy = ListNode()
        cur = dummy
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                cur.next = temp1
                temp1 = temp1.next
            else:
                cur.next = temp2
                temp2 = temp2.next
            cur = cur.next
        if temp2:
            cur.next = temp2
        if temp1:
            cur.next = temp1
        return dummy.next
