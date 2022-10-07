# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        count = 0
        q=deque([root])
        BFS=[]
        while q:
            
            level = []
            
            if count == 0:
                count=1
            else:
                count=0
            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                        
                val = node.val
                level.append(val)
                
            if count == 1:
                BFS.append(level)
            else:
                BFS.append(level[::-1])
        return BFS                            
        
            