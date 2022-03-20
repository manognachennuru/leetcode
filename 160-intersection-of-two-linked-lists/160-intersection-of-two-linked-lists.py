# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, HeadA: ListNode, HeadB: ListNode) -> Optional[ListNode]:
        
        #a+l+b = b+l+a
        a = HeadA
        b = HeadB
        
        #finding out the intersection
        while a != b:
            a = HeadB if a == None else a.next
            b = HeadA if b == None else b.next
        return a if a == b else None
        

        