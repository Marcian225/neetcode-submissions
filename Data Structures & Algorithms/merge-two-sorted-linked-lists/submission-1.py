# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = list1
        p2 = list2

        dummy = ListNode()

        current = dummy

        while p1 and p2:
            if p1.val < p2.val:
                current.next = p1
                current = p1
                p1 = current.next
            else:
                current.next = p2
                current = p2
                p2 = current.next

        current.next = p1 if p1 else p2

        return dummy.next