"""
133. Clone Graph
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # 97.73% | 16.12%
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        known_graph = {}

        def cloner(node_to_clone):
            if node_to_clone.val in known_graph:
                return known_graph[node_to_clone.val]

            copy_node = Node(val=node_to_clone.val)
            known_graph[copy_node.val] = copy_node

            for neighbor in node_to_clone.neighbors:
                copy_node.neighbors.append(cloner(neighbor))

            return copy_node

        return cloner(node) if node else None
