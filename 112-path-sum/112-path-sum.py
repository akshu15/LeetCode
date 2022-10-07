# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return []
        
        q = deque([root])
        BFS = []
        
        while q:
            
            level = []
            
            for i in range(len(q)):
                
                node = q.popleft()
                
                if node:
                    if node.left: 
                        val = node.left.val + node.val
                        node.left.val = val
                        q.append(node.left)
                        
                    if node.right: 
                        val = node.right.val + node.val
                        node.right.val = val
                        q.append(node.right)
                        
                    if not node.left and not node.right:
                        if node.val == targetSum:
                            return True
                # print(q)
                        
                level.append(node)
            BFS.append(level)
            # print(BFS)
        if len(BFS)==1 and BFS[0][0].val ==targetSum:
            return True
        return
        