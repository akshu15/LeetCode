# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        #0<=pos<=length(list)
        
        #find the length
        
        if head==None:
            return
        itr=ListNode()
        itr=head
        hashMap={}
        
        while itr.next: #iterate through the linked list till reaches end
            
            if itr not in hashMap:
                hashMap[itr]=itr.val
                itr=itr.next
            else:
                return True
                
        
        
#         count=0
        
#         pos1=pos
        
#         if count==pos1:  #at head is the pos
#             return 
        
#         elif pos==-1:
#             return 
        
#         print(itr)
        
#         while itr.next: #iterate through the linked list till reaches end
            
#             if count==pos:
#                 break
#             else:
#                 itr=itr.next
#                 count+=1