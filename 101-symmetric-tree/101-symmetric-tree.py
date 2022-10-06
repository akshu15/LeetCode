# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def leftHelper(root, output):
            
            if root:
                leftHelper(root.left, output)
                output.append(root.val)
                leftHelper(root.right, output)
            output.append("null")
            
        def rightHelper(root, output):
            
            if root:
                rightHelper(root.right, output)
                output.append(root.val)
                rightHelper(root.left, output)
            output.append("null")
            
        l,r = [],[]
        leftHelper(root.left,l)
        rightHelper(root.right,r)
        if l==r:
            return True