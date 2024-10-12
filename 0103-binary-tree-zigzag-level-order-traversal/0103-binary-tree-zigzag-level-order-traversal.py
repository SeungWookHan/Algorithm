# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        
        def zigzag(root: Optional[TreeNode], level):
            if not root:
                return
            if len(result) <= level:
                result.append([])
            
            if level % 2 == 0:
                result[level].append(root.val)
            else:
                result[level].insert(0, root.val)
            
            zigzag(root.left, level+1)
            zigzag(root.right, level+1)
            
        zigzag(root, 0)
        return result