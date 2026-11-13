# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])

        if root == None:
            return None

        while q:
            for _ in range(len(q)):
                i = q.popleft()
                i.left, i.right = i.right, i.left
                if i.left != None:
                    q.append(i.left)
                if i.right != None:
                    q.append(i.right)

        return root
