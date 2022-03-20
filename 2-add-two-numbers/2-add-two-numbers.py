# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p = l1
        q = l2
        carry = 0
        dummy = ListNode(0)
        head = curr = ListNode(0)
        
        while p != None or q != None:
            if p == dummy and q == dummy:
                break
                
            sum =  p.val + q.val + carry
            curr.next = ListNode(sum % 10)
            carry = sum // 10
            
            p = dummy if p.next == None else p.next
            q = dummy if q.next == None else q.next    
            curr = curr.next
        
        curr.next = ListNode(carry) if carry else None
        return head.next
            