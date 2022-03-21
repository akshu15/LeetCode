# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        i=0
        hashMap={}
        
        def zigzag(root,i):
            
            if root==None:
                return
            
            if i in hashMap:
                hashMap[i].append(root.val)
            else:
                hashMap[i]=[root.val]
            
            zigzag(root.left,i+1)
            zigzag(root.right,i+1)
                
            # print(hashMap)
            
        zigzag(root,i)
        
        mylist=[]
        
        def rever(rlist):
            element=[]
            for i in range(len(rlist)-1,-1,-1):
                element+=[rlist[i]]
            
            print(element)
            return(element)
        
        # print(mylist)
        
        el=0
     
        while (el<len(hashMap.values())-1):
            mylist.append(hashMap[el])
            mylist.append(rever(hashMap[el+1]))
            el=el+2
            
        if el==len(hashMap.values())-1:
            mylist.append(hashMap[el])  
            
        return(mylist)
        
            