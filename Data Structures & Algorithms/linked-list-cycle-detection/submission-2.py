# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None or head.next == None:
            return False

        slow = head
        fast = head.next
        while slow and fast:
            slow = slow.next
            fast = fast.next
            if fast == None or fast.next == None:
                return False
            else:
                fast = fast.next
            if slow == fast:
                return True