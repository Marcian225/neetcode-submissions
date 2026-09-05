# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root == None:
            return True

        stack = [root]

        seen = {None: 0}

        while stack:

            node = stack[-1]

            if node.left and node.left not in seen:
                stack.append(node.left)
            elif node.right and node.right not in seen:
                stack.append(node.right)
            else:
                node = stack.pop()

                leftheight = seen[node.left]
                rightheight = seen[node.right]

                if abs(rightheight-leftheight) > 1:
                    return False

                seen[node] = 1+ max(leftheight,rightheight)

        return True



