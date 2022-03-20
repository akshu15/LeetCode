# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # print(list1)
        dummy = ListNode()
        newlist = dummy
        while(list1!=None and list2 !=None): #until any of the list reaches the end
            
            if (list1.val<=list2.val):
                newlist.next=list1
                # print(list1)
                newlist = newlist.next
                list1=list1.next
            else:
                newlist.next=list2
                newlist = newlist.next
                list2=list2.next
                # print(newlist)
                
                
            
        
        if list1==None:
            newlist.next=list2
            
        elif list2==None:
            newlist.next=list1
        
        return dummy.next
        