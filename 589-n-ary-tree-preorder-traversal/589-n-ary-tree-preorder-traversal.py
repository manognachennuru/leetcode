"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return None
        output = []
        output += [root.val]
        for node in root.children:
            output += self.preorder(node)
        return output