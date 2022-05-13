# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def go(root):
            if root==None:
                return 0
            else:
                h1=root.left
                h2=root.right
                return 1+max(go(h1),go(h2))
        return go(root)