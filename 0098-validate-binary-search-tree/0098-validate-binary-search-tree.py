# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidate(self, root, min, max):
        if not root:
            return True
        elif (min is not None and min >= root.val) or (max is not None and max <= root.val):
            return False
        else:
            return self.isValidate(root.left, min, root.val) and self.isValidate(root.right, root.val, max)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidate(root, None, None)
            