# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        i=0
        hashMap={}
        
        def findroot(root,i):
            if root==None:
                return
            
            if i in hashMap:
                hashMap[i].append(root.val)
            else:
                hashMap[i] = [root.val]
            
            findroot(root.left, i+1)
            findroot(root.right,i+1)
            
        
        findroot(root,i)
        
        return(list(hashMap.values()))
        
#         print(root.left)
#         print(root.right)
#         element=[]
#         mylist=[]
        
        
#         element+=[root.left.val]
#         element+=[root.right.val]
        
#         mylist.append(element)
        # print(mylist)
        
#         if root:
#             element+=[root.val]

#             mylist.append(element)
#             element=[]
#             index=0
#             itr=root
            
#             while itr:
                
#                 if root.left and index==0:
#                     element+=[root.left.val]
#                     index=1

#                 if root.right and index==1:
#                     element+=[root.right.val]
#                     index=0

#                 mylist.append(element)
#                 itr=itr
        
#             print(mylist)
            
#         else:
#             return




