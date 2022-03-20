# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        #finding the length and tail of the linkedlist
        length = 0
        curr = tail = head
        while curr != None:
            length += 1
            tail = curr
            curr = curr.next
        
            
        dummy = prev = ListNode(0,head)
        curr = head
        
        for _ in range(0,length):
            
            if curr.val >= x:
                #if node to be removed is the (actual) tail 
                #==> it needs to be appended at same place, hence we can return
                if curr == tail and tail.next == None:
                    return dummy.next
                
                #remove the node from here, append at the (new) tail
                prev.next = curr.next
                curr.next = None
                tail.next = curr
                tail = curr
                
                #to accomplish next iterations
                curr = prev.next
                
            else:
                curr = curr.next
                prev = prev.next
            
        return dummy.next
            
                
                
        