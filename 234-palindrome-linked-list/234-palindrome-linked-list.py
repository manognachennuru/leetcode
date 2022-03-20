# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        if head==None or head.next==None:
            return head
        pre = head
        current =head.next
        while current:
            next_node = current.next
            current.next = pre
            pre = current
            current = next_node
        head.next = None
        return pre
    def isPalindrome(self, head: ListNode) -> bool:
        
        if head==None or head.next==None:
            return True
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow = self.reverse(slow) 
        fast = head
        
        while slow!=None:
            if slow.val!=fast.val:
                return False
            slow=slow.next
            fast=fast.next
        return True