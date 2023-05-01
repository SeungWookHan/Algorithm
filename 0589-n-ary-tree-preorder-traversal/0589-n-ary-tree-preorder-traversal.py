"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        self.dfs(root, result)
        return result
    
    def dfs(self, root, result):
        if not root:
            return
        result.append(root.val)
        for v in root.children:
            self.dfs(v, result)
        