# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,head: Optional[ListNode]):
        if head == None or head.next == None:
            return head
        
        prev = head
        curr = head.next
        head.next = None
        
        while curr.next != None:
            temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp
            
        curr.next = prev
        #print("reversed second half is", curr)
        return curr
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        #find second half of the linkedlist
        
        left = right = head
        while right != None and right.next != None:
            left = left.next
            right = right.next.next
            
        right = left.next    
        left.next = None 
        
        first = head
        second = self.reverseList(right)
        #print("first half is ",first)
        #print("second half is ", second)
        
        while first != None and second != None:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2
            
            
            
        
        
        
        
            
        