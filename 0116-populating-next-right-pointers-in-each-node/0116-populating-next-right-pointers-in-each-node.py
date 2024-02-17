"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #can't do with dfs, use bfs
        #level order traversal and find out each level 
        if not root:
            return root
        q = deque()
        q.append(root)
        root.next =  None
        
        while True: #break it when you're done with all nodes
            currLevel = deque() #store current level
            
            while q:
                #print([x.val for x in q])
                node = q.popleft()
                if node.left and node.right:
                    currLevel.append(node.left)
                    currLevel.append(node.right)
                
            #no elements in currLevel
            if len(currLevel) == 0:
                break
                
            #now we found currLevel
            for i in range(len(currLevel)-1):
                #point to next
                currLevel[i].next = currLevel[i+1]
                
            q = q + currLevel.copy()
            currLevel[-1].next = None
        
        return root



