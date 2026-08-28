# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = dict()

        
        if head == None or head.next == None:
            return False

        node = head
        index = 0
        while node:
            if node in visited:
                return True
            else:
                visited[node] = index
                node = node.next
                index +=1
        return False
