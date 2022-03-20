# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #insert at the beginning 
        
        if head==None:
            return
        else:
        
            itr = head #used to iterate our linkedlist
            head2=ListNode() #create a listnode to create new linked list
            head2 = head2.next

            while itr:
                # print(itr.val)
                    
                node=ListNode(itr.val)
                node.next=head2
                head2=node
                # print(node)

                itr=itr.next
            # print(head2)

            return head2
            
        