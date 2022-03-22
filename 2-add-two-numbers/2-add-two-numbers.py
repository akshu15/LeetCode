# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if l1==None:
            return l2
        elif l2==None:
            return l1
        elif l1==None and l2==None:
            return
        else:
            
            carryon=0
            head=ListNode()
            itr=head
            
            while l1!=None and l2!=None:
                
                str1=""
                
                if carryon ==1:
                    total=l1.val + l2.val+1
                else:
                    total=l1.val + l2.val
                
                str1+=str(total)
                mylist=list(str1)
                
                # print(mylist[0]+1)
                
                if len(mylist)>1:
                    
                    carryon=1
                    node=ListNode(int(mylist[1]))
                    
                else:
                    if carryon==1:
                        carryon=0
                    node=ListNode(int(mylist[0]))
                # print(head)
                if head==None:
                    head=node
                    itr=head
                else: 
                    itr.next=node
                    itr=itr.next
                l1=l1.next
                l2=l2.next
            
                
            if l1!=None:
                while l1:
                    if carryon==1:
                        total=l1.val+1
                        str1=str(total)
                        mylist=list(str1)
                        
                        if total>9:
                            carryon=1
                            node=ListNode(int(mylist[1]))
                        else:
                            carryon=0
                            node=ListNode(int(mylist[0]))
                        itr.next=node
                        itr=itr.next
                    else:
                        node=ListNode(l1.val)
                        if head==None: 
                            head=node
                            itr=head
                        else:
                            itr.next=node
                            itr=itr.next
                        
                    l1=l1.next
                    
            if l2!=None:
                while l2:
                    if carryon==1:
                        total=l2.val+1
                        str1=str(total)
                        mylist=list(str1)
                        
                        if total>9:
                            carryon=1
                            node=ListNode(int(mylist[1]))
                        else:
                            carryon=0
                            node=ListNode(int(mylist[0]))
                        itr.next=node
                        itr=itr.next
                    else:
                        node=ListNode(l2.val)
                        if head==None: 
                            head=node
                            itr=head
                        else:
                            itr.next=node
                            itr=itr.next
                        
                    l2=l2.next
                    
            if carryon==1:
                itr.next=ListNode(1)
                    
                    
        return(head.next)       
    
        
#         str1="10"
        
#         my=list(str)
        
#         print(my[0])
        