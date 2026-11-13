# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return -1000, -1000
            # if not node.left and not node.right:
            #     return node.val, node.val
            
            l_p, l_m = dfs(node.left)
            r_p, r_m = dfs(node.right)
            
            path = max(l_p + node.val, r_p + node.val, node.val)
            max_p = max(l_m, r_m, l_p + r_p + node.val, path)

            return path, max_p
        
        return dfs(root)[1]