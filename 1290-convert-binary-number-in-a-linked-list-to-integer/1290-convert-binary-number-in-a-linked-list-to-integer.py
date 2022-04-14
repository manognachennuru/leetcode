# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        curr = head
        ans = 0
        while curr != None:
            ans = ans*2 + curr.val
            curr = curr.next
            
        return ans
        