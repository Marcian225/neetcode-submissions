# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        arr = []
        current = list1
        while current:
            arr.append(current.val)
            current = current.next

        current = list2
        while current:
            arr.append(current.val)
            current = current.next

        arr.sort()
        print(arr)

        dummy = ListNode()
        current=dummy
        for x in arr:
            current.next  = ListNode(x)
            current = current.next
        return dummy.next 