# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head==None:
            return
        itr=ListNode()
        itr=head
        hashMap={}
        
        while itr.next: #iterate through the linked list till we reache the end
            
            if itr not in hashMap:
                hashMap[itr]=itr.val
                itr=itr.next
            else:
                return True
