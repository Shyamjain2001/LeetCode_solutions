# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def go(root):
            if root==None:
                return 0
            h1=root.left
            h2=root.right
            if h1==None:
                if h2==None:
                    return 1
                return 1+go(h2)
            elif h2==None:
                return 1+go(h1)
            else:
                return 1+min(go(h1),go(h2))
        return go(root)
        