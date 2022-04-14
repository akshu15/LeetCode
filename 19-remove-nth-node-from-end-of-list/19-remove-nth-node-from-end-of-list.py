# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #find length of the node using head
        #target = length - n
        #again start from head and go till target(i==target)
        
        
        itr1=head
        length=1
        while itr1:
            length+=1
            itr1=itr1.next
        
        target=length-n
        
        itr=head
        count=1
        
        if count==target:
            head=head.next
        else:
            while itr:

                if (count+1)==target:
                    itr.next=itr.next.next
                    break
                else:
                    itr=itr.next
                    count+=1
        return head
            
            
            
            