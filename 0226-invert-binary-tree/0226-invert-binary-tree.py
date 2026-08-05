# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:    #necessario cosi non hai q=[None]
            return None

        q = deque([root])
        res = root

        while q:    # NB: una coda che contiene None NON è una coda vuota
            node = q.popleft()
            left = node.left
            right = node.right

            if left: q.append(left)
            if right: q.append(right)
            node.left, node.right = right, left
        
        return res