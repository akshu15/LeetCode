# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        q = deque([root])
        BFS=[]
        
        while q:
            
            level = []
            
            for i in range(len(q)):
                
                node = q.popleft()
                
                if node:
                    if node.left: 
                        q.append(node.left) 
                        
                    if node.right:
                        q.append(node.right) 
                        
                val = node.val 
                level.append(val) 
                
            BFS.append(level)
        return BFS[::-1]
        