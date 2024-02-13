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
        #how do i clone a graph
        #dfs - go to all nodes, create a node 
        #for neighbor in neighbors, create an edge, call dfs on that neighbor
        
#         printed = set()
#         def displayGraph(node):
#             if node in printed:
#                 return
#             printed.add(node)
#             print(node.val)
#             for neighbor in node.neighbors:
#                 print("--> ", neighbor.val)
#             for neighbor in node.neighbors:
#                 displayGraph(neighbor)
                
        seen = {}
        def dfs(snode, tnode):
            seen[tnode.val] = tnode
            
            sneighbors = snode.neighbors
            for sneighbor in sneighbors:
                if seen.get(sneighbor.val):
                    #neighbor already seen
                    tneighbor = seen[sneighbor.val]
                    tnode.neighbors.append(tneighbor)
                    #tneighbor.neighbors.append(tnode)
                
                    continue
                    
                tneighbor = Node(sneighbor.val)
                tnode.neighbors.append(tneighbor)
                #tneighbor.neighbors.append(tnode)
                
                dfs(sneighbor, tneighbor)
         
        
        if node == None:
            return None
        
        tnode = Node(node.val)
        dfs(node, tnode)
        # print("printing node")
        # displayGraph(node)
        # print("printing tnode")
        # displayGraph(tnode)
        
        return tnode