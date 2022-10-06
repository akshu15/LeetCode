# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def helper(node, output):
            
            if node:
                helper(node.left, output)
                output.append(node.val)
                helper(node.right, output)
                
            output.append("null")
            
        pOutput, qOutput = [], []
        helper(p, pOutput)
        helper(q, qOutput)
        
        if pOutput == qOutput:
            return True
        