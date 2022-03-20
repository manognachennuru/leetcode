# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #going to middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        reversedHalf = self.reverse(slow)
        return self.areEqual(head,reversedHalf)
            
    def reverse(self,head):
        curr = head
        prev = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev
            
    def areEqual(self,first,second):
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
            
            
        return True