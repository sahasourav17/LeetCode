"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':


        # for mapping of old node to new node
        oldToNew = {}

        def clone(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbors in node.neighbors:
                copy.neighbors.append(clone(neighbors))
            return copy
        return clone(node) if node else None

