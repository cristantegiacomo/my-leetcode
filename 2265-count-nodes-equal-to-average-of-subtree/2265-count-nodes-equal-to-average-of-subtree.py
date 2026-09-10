# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return (0, 0)

            sumL, numL = dfs(node.left)
            sumR, numR = dfs(node.right)

            avg = (sumL + sumR + node.val) // (numR + numL + 1)

            if node.val == avg:
                res += 1

            return (node.val + sumL + sumR, 1 + numL + numR)

        dfs(root)
        return res