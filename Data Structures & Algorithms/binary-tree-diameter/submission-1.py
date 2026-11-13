# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # res = 0
        # def dfs(node):
        #     if not node:
        #         return 0
            
        #     left = dfs(node.left)
        #     right = dfs(node.right)
            
        #     nonlocal res
        #     res = max(res, left + right)
        #     return max(left, right) + 1

        # dfs(root)
        # return res



        # inside function itself
        def dfs(node):
            if not node:
                return 0, 0
            
            leftp, leftd = dfs(node.left)
            rightp, rightd = dfs(node.right)

            diam = max(leftd, rightd, leftp + rightp)
            height = max(leftp, rightp) + 1

            return height, diam

        
        return dfs(root)[1]



