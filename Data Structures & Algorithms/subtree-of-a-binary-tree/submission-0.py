# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs1(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2 or root1.val!=root2.val:
                return False
            left=dfs1(root1.left,root2.left)
            right=dfs1(root1.right,root2.right)

            return left and right
        def dfs(curr):
            if not curr:
                return False
            
            
            if curr.val==subRoot.val:
                return dfs1(curr,subRoot)

            return dfs(curr.left) or dfs(curr.right)
        return dfs(root)
            