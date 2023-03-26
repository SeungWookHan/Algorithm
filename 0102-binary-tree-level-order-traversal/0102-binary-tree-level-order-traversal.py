# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue, result = deque(), []
        if not root:
            return []
        
        queue.append(root)
        
        while len(queue) != 0:
            level = []
            for _ in range(len(queue)):
                parent = queue.popleft()
                level.append(parent.val)
                
                if parent.left:
                    queue.append(parent.left)
                if parent.right:
                    queue.append(parent.right)
            result.append(level)
        return result
            