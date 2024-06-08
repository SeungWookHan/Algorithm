# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, answer):
            if not root:
                return
            dfs(root.left, answer)
            answer.append(root.val)
            dfs(root.right, answer)
        answer = []
        dfs(root, answer)
        return answer