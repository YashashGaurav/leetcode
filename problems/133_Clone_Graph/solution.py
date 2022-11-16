'''
    133. Clone Graph
'''


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Graph: # for testing

    def __init__(self):
        self.make_graph()

    def make_graph(self):
        self.nodes = [
            Node(1, neighbors=None),
            Node(2, neighbors=None),
            Node(3, neighbors=None),
            Node(4, neighbors=None)
        ]
        self.root = self.nodes[0]
        self.add_neighbors()

    def add_neighbors(self):
        self.nodes[0].neighbors = [self.nodes[1], self.nodes[3]]
        self.nodes[1].neighbors = [self.nodes[0], self.nodes[2]]
        self.nodes[2].neighbors = [self.nodes[1], self.nodes[3]]
        self.nodes[3].neighbors = [self.nodes[0], self.nodes[2]]

    def get_root(self):
        return self.root


class Solution:
    # assumes that all nodes are connected.
    # case [[2,3],[1],[1]] would fail
    # I don't understand what [1] signifies here
    def cloneGraph0(self, node: 'Node') -> 'Node':
        if not node:
            return None

        root = None

        visited = {}

        to_visit = []
        to_visit.append(node)

        while to_visit:
            curr = to_visit.pop()
            curr_copy = Node(curr.val)
            visited[curr_copy.val] = curr_copy

            for n in curr.neighbors:
                if n.val in visited:
                    curr_copy.neighbors.append(visited[n.val])
                    visited[n.val].neighbors.append(curr_copy)
                else:
                    to_visit.append(n)
                    break

            if not root:
                root = curr_copy
            
        return root

    # Accepted	91 ms	14.4 MB - neetcode 
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}

        def clone(node):
            if node in visited:
                return visited[node]

            copy = Node(node.val)
            visited[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            
            return copy
        
        return clone(node) if node else None


Solution().cloneGraph(Graph().get_root())



