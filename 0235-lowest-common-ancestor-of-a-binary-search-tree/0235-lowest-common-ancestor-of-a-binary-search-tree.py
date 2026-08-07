# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        qq = deque([root])

        while qq:
            node = qq.popleft()

            if ((p.val >= node.val and q.val <= node.val) or
                (p.val <= node.val and q.val >= node.val)):
                return node

            if node.left: qq.append(node.left)
            if node.right: qq.append(node.right)     