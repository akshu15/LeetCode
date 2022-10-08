# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return TreeNode().left
        if not root.left and not root.right:
            return root
        q = deque([root])
        BFS=[]
        
        while q:
            
            level = []
            
            for i in range(len(q)):
                
                node = q.popleft()
                
                temp = node.left
                node.left = node.right
                node.right = temp
                
                if node:
                    if node.left: 
                        q.append(node.left) 
                        
                    if node.right:
                        q.append(node.right) 
                        
                val = node.val 
                level.append(val) 
                
            BFS.append(level)
        return(root)
            