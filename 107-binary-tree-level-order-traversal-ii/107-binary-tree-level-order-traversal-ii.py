# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        hashMap={}
        i=0
        
        def treeTraverse(root,i):
            
            if root==None:
                return
            
            if i in hashMap:
                hashMap[i].append(root.val)
            else:
                hashMap[i]=[root.val]
                
            treeTraverse(root.left, i+1)
            treeTraverse(root.right, i+1)
            
            
        treeTraverse(root,i)
        # print(hashMap)
        mylist=[]
        
        for i in range(len(hashMap.values())-1,-1,-1):
            
            mylist.append(hashMap[i])
            
        return(mylist)