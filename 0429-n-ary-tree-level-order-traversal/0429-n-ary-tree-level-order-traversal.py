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
        seen = set()
        result = []
        
        q.append(root)
        seen.add(root)
        result.append([root.val])
        
        while True: #make sure to break
            curLevel = []
            
            while q:
                node = q.popleft() #always popleft for queue
                
                for c in node.children:
                    if c not in seen and c != None:
                        curLevel.append(c)
                        seen.add(c)
            
            #no nodes in this level
            if len(curLevel) == 0:
                break
            
            #we have one level in curLevel
            result.append(list([c.val for c in curLevel]))
            
            #now add curLevel to q
            q.extend(curLevel)
                    
        return result
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
        