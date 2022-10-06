# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def helper(root, output):
            if root:
                helper(root.left,output)
                output.append(root.val)
                helper(root.right,output)
            
        output=[]
        if root:
            helper(root, output)
        return(output)