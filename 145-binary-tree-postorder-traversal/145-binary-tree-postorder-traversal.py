# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def helper(root, output):
            if root:
                helper(root.left, output)
                helper(root.right, output)
                output.append(root.val)
            
        
        output = []
        
        helper(root, output)
        return(output)
        