# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        itr=head
        
        while itr:
            n_next=itr.next
            
            if itr==head and itr.val==val:
                head=n_next
                itr=itr.next
                
            else:
                if n_next!=None and n_next.val==val:
                    itr.next=n_next.next
                else:
                    itr=itr.next
                    
            
       
            
        return(head)