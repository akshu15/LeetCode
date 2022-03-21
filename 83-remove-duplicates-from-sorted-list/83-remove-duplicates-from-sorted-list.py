# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head==None or head.next==None:
            return head
        else:
            itr = head
            count=0
            n_next=itr.next
            

            while n_next.next!=None:

                n_next=itr.next

                if itr==head and n_next.val==itr.val:
                    head=n_next
                    itr=itr.next
                    # print(head)

                elif n_next.next!=None:
                
                    if n_next.val==itr.val:
                        itr.next=n_next.next
                    else:
                        itr=itr.next

            # print(itr.val)
            if n_next.next==None and n_next.val==itr.val:
                itr.next=None



            # if itr==None and itr.val==

            return(head)