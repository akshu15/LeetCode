# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists)>0:
        
            # print(lists)
            element=[]
            mylist=[]

            hashMap={}

            for i in lists:
                element+=[i]
            # print(element)

            for i in range(len(element)):
                value=element[i]
                while value:
                    print(value.val)
                    mylist+=[value.val]
                    value=value.next
          
            length=len(mylist)
            if length>0:
                mylist.sort() 
           
                node=ListNode(mylist[0])
                head=node
                itr=head
                for i in range(1,length):

                    node=ListNode(mylist[i])
                    if head.next==None:
                        head.next=node
                    else:
                        itr.next=node
                    itr=itr.next

            else:
                return
            return(head)   #dont print mylist.sort here
        else:
            return
      