# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.i = 0  
        self.ret = 0 
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder = left -> self -> right
        self.inorder(root, k)
        return self.ret
        
    def inorder(self, root: Optional[TreeNode], k: int):
        if not root:
            return

        self.inorder(root.left, k)
        self.i += 1
        if self.i == k:
            self.ret = root.val
            return
        self.inorder(root.right, k)