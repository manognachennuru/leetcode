# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #tortoise and hare algorithm
        if head == None:
            return False
        
        slow = ListNode(0,head)
        fast = head
        while fast != None and fast.next != None:
            if slow == fast:
                return True
            
            slow = slow.next
            fast = fast.next.next
        return False