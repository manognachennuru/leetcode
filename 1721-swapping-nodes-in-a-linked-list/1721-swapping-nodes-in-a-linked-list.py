# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        slow = dummy
        fast = dummy
        for _ in range(0,k):
            fast = fast.next
        #store kth node 
        kth = fast
        while fast != None:
            slow = slow.next
            fast = fast.next
            
        kth_from_end = slow
        
        kth.val, kth_from_end.val = kth_from_end.val, kth.val
        
        return dummy.next