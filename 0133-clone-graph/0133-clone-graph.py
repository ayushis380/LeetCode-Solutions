"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {} # making a map for old to new (new has clone)
        def clone(node):
            if node in oldToNew:
                return oldToNew[node] # if already there in map then clone already made, return clone copy
            copy = Node(node.val)
            oldToNew[node] = copy 
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei)) # for each neighbors of node append to copy neighbors
            return copy
        
        return clone(node) if node else None