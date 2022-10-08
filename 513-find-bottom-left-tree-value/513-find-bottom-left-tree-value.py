# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        
        if not root.left and not root.right:
            return root.val
        q = deque([root])
        BFS=[]
        n_arr=[]
        
        while q:
            
            level = []
            n=[]
            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    if node.left: 
                        q.append(node.left)
                        
                    if node.right:
                        q.append(node.right) 
                        
#                 if not node.left: 
#                     n.append(None) 
#                 else: 
#                     n.append(node.left.val)
                    
                
#                 if not node.right: 
#                     n.append(None)
#                 else: 
#                     n.append(node.right.val)
                # print(n)
                val = node.val
                level.append(val) 
                
            BFS.append(level)
            # n_arr.append(n)
        # print(n_arr[-2])
        # lastLevel=n_arr[-2]
        # for i in range(len(lastLevel)):
        #     if lastLevel[i] is not None:
        #         return(lastLevel[i])
        print(BFS)
        return BFS[-1][0]
