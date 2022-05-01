# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        # dfs (28ms, 13.5MB)
        # def dfs_invert(node):
        #     if node is None:
        #         return
        #     placeholder = node.left
        #     node.left = node.right
        #     node.right = placeholder
        #
        #     dfs_invert(node.left)
        #     dfs_invert(node.right)
        #
        # dfs_invert(root)

        # bfs (14ms, 13.3MB) (much faster, 94.13% faster and 94.68% less memory)
        # This can be changed to dfs by changing popleft to pop
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node is None:
                continue
            placeholder = node.left
            node.left = node.right
            node.right = placeholder

            q.append(node.left)
            q.append(node.right)

        return root
