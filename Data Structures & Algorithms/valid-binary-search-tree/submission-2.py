# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        cur = float('-inf')
        inValid = False

        def dfs(root):
            nonlocal inValid
            nonlocal cur
            if not root or inValid:
                return
            
            if root.left:
                dfs(root.left)
            
            if cur >= root.val:
                inValid = True
            else:
                cur = root.val
                
            if root.right:
                dfs(root.right)
        
        dfs(root)
        return not inValid