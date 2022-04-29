
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

        hist = {}
        cloneHead = Node(node.val)

        def dfs(node, cloneNode):
            if node in hist:
                return

            hist[node] = cloneNode

            for i in range(len(cloneNode.neighbors)):
                if node[i] in hist:
                    cloneNode.neighbors.append(hist[node[i]])
                else:
                    copy = Node(node[i].val)
                    cloneNode.neighbors.append(copy)
                    hist[node[i]] = copy
                    dfs(node.neighbors[i], cloneNode.neighbors[i])

        dfs(node, cloneHead)
        return cloneHead


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


