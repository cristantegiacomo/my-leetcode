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

            curr_sum = node.val + sumL + sumR
            curr_num = 1 + numR + numL

            if node.val == curr_sum // curr_num:
                res += 1

            return (curr_sum, curr_num)

        dfs(root)
        return res