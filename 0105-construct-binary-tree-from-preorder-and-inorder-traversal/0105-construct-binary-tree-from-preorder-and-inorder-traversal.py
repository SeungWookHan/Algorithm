# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: 루트 -> 왼 -> 오
        # inorder: 왼 -> 루트 -> 오
        
        if not preorder or not inorder:
            return
        
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        
        inorder_index = inorder.index(root_val)
        
        root.left = self.buildTree(preorder, inorder[:inorder_index])
        root.right = self.buildTree(preorder, inorder[inorder_index+1:])
        
        return root