# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        q = deque([root])
        BFS=[]
        found = 0
        
        while q:
            
            level = []
            
            for i in range(len(q)):
                
                node = q. popleft()
                
                if node:
                    if not node.right and not node.left:
                        found = 1
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                        
                level.append(node.val)

            BFS.append(level)
            if found==1:
                return(len(BFS))