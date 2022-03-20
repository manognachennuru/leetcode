# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, HeadA: ListNode, HeadB: ListNode) -> Optional[ListNode]:

        #finding if they intersect. (checking whether tails are equal)
        a_tail = HeadA
        b_tail = HeadB
        while a_tail.next != None:
            a_tail = a_tail.next
        while b_tail.next != None:
            b_tail = b_tail.next
        
        #no intersection
        if a_tail != b_tail:
            return 
        
        #they intersect
        #a+l+b = b+l+a
        a = HeadA
        b = HeadB
        
        #finding out the intersection
        while a != None and b != None:
            if a == b:
                return a
            
            a = HeadB if a.next == None else a.next
            b = HeadA if b.next == None else b.next

        