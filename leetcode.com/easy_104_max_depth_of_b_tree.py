# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, depth):
            dl, dr = depth, depth
            if node.left:
                dl = dfs(node.left, depth + 1)
            if node.right:
                dr = dfs(node.right, depth + 1)

            return max(dl, dr)

        return dfs(root, 1) if root is not None else 0
