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
        #hashmap with old and new nodes
        #dfs, create clone if it's not in hashmap, 
        #add edges while doing dfs
        
        dic = {}
        
        def dfs(node):
            if node == None:
                return
            if node in dic:
                return dic[node]
            clone_node = Node(node.val)
            dic[node] = clone_node
            
            for nei in node.neighbors:
                clone_nei = dfs(nei)
                clone_node.neighbors.append(clone_nei)
            
            return clone_node
        
        n = dfs(node)
        return n