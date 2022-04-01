# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        l=[]
        
        def Traversal(root,l):
            if root!=None:
                Traversal(root.left,l)
                l.append(root.val)
                Traversal(root.right,l)
                
            return l
                
        return Traversal(root,l)