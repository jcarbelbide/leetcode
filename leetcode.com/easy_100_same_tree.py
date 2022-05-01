# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        pq = deque()
        qq = deque()

        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        pq.append(p)
        qq.append(q)

        while pq and qq:
            p = pq.popleft()
            q = qq.popleft()

            if p is None and q is None:
                continue
            if p is None or q is None:
                return False

            if p.val != q.val:
                return False

            pq.append(p.left)
            pq.append(p.right)

            qq.append(q.left)
            qq.append(q.right)

        return True if len(pq) == 0 and len(qq) == 0 else False
