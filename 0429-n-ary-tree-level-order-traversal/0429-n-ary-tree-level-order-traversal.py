"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        #level order traversal
        if root == None:
            return []
        
        q = deque()
        result = []
        
        q.append(root)
        
        while q:
            curLevel = []
            length = len(q)
            
            for i in range(0, length):
                node = q.popleft() #always popleft for queue

                q.extend(node.children)
                curLevel.append(node.val)
             
            result.append(curLevel.copy())
            curLevel = []
                    
        return result
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
        