# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1==None and list2==None:
            return
        elif list1==None:
            return list2
        elif list2==None:
            return list1
        
        else:
            if list1.val<=list2.val:
                node=ListNode(list1.val)
                list1=list1.next
            else:
                node=ListNode(list2.val)
                list2=list2.next
                
            head=node
            itr=head
            
            
            while list1!=None and list2!=None:
                # print(head)
                
                if list1.val<=list2.val:
                    node=ListNode(list1.val)
                    list1=list1.next
                else:
                    node=ListNode(list2.val)
                    list2=list2.next
                    
                if head.next==None:
                    head.next=node
                else:
                    itr.next=node
                itr=itr.next
                    
            
            if list1!=None and list2==None:
                while list1!=None:
                    itr.next = list1
                    list1 = list1.next
                    itr = itr.next
            
            if list2!=None and list1==None:
                while list2!=None:
                    itr.next = list2
                    list2 = list2.next
                    itr = itr.next
                    
                
            print(head)
            return head
            # print(node)
    
        