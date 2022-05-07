
from collections import deque

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return None

        clone_head = Node(node.val)
        hist = {node.val: clone_head}
        q_clone = deque()
        q_origin = deque()
        q_clone.append(clone_head)
        q_origin.append(node)

        while q_origin:
            clone_node = q_clone.popleft()
            origin_node = q_origin.popleft()

            for nei in origin_node.neighbors:
                if nei.val not in hist:
                    hist[nei.val] = Node(nei.val)
                    q_clone.append(hist[nei.val])
                    q_origin.append(nei)
                clone_node.neighbors.append(hist[nei.val])

        return clone_head


def print_node(node, hist):
    hist[node] = 1
    # print(node, node.val, node.neighbors[0].val, node.neighbors[1].val, len(node.neighbors))
    print(node)
    for nei in node.neighbors:
        if nei not in hist:
            print_node(nei, hist)


if __name__ == '__main__':
    node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)

    node1.neighbors = [
        node2,
        node4,
    ]
    node2.neighbors = [
        node1,
        node3,
    ]
    node3.neighbors = [
        node2,
        node4,
    ]
    node4.neighbors = [
        node1,
        node3,
    ]

    clone = Solution.cloneGraph(1, node1)
    print_node(clone, {})


