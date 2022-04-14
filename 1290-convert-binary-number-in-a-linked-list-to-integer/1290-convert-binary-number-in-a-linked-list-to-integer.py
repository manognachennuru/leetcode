# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        #find length of the linkedlist
        tmp = head
        count = 0
        while tmp != None:
            count += 1
            tmp = tmp.next
        
        curr = head
        ans = 0
        while curr != None:
            ans += curr.val*pow(2,count-1)
            count -= 1
            curr = curr.next
            
        return ans
        