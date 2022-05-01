# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        q = deque()

        if root is None:
            return []

        q.append([root, 0])
        current_level = 0
        level_list = []
        res = []
        while q:
            [node, level] = q.popleft()

            if node is None:
                continue

            if level == current_level:
                level_list.append(node.val)
            else:
                res.append(level_list)
                current_level = level
                level_list = []
                level_list.append(node.val)

            q.append([node.left, current_level + 1])
            q.append([node.right, current_level + 1])

        res.append(level_list)

        return res
