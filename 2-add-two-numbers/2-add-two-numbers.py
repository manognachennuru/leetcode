# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = l1
        q = l2
        carry = sum = 0
        head = curr = ListNode(0)
        
        while p != None or q != None:
            if p:
                sum += p.val
                p = p.next
            if q:
                sum += q.val
                q = q.next
            
            sum += carry
            
            curr.next = ListNode(sum % 10)
            carry = sum // 10
            curr = curr.next
            sum = 0
        
        curr.next = ListNode(carry) if carry else None
        return head.next
            