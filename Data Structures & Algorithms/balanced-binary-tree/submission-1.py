# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True,0]
            root.right=dfs(root.right)
            root.left=dfs(root.left)
            balanced=abs(root.right[1]-root.left[1])<=1 and root.left[0] and root.right[0]
            return[balanced,1+max(root.right[1],root.left[1])]
        return dfs(root)[0]