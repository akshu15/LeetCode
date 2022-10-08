# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val,None,None)
        
        if depth == 1:
            newNode = TreeNode(val,root,None)
            return newNode
        q = deque([root])
        BFS =[]
        count = 1
        while q:
            level = []
            
            for i in range(len(q)):
                
                node = q.popleft()
                   
                if node:
                    if node.left:
                        if count==depth-1:
                            newNode = TreeNode(val,None,None)
                            temp = node.left
                            node.left = newNode
                            newNode.left = temp
                        q.append(node.left)
                    if not node.left and count==depth-1:
                            newNode = TreeNode(val,None,None)
                            node.left = newNode

                    if node.right:
                        if count==depth-1:
                            newNode = TreeNode(val,None,None)
                            temp = node.right
                            node.right = newNode
                            newNode.right = temp
                        q.append(node.right)
                        
                    if not node.right and count==depth-1:
                            newNode = TreeNode(val,None,None)
                            node.right = newNode
                            
                    if not node.left and not node.right and count == depth-1:
                        newNode = TreeNode(val,None,None)
                        node.left = newNode
                        node.right = newNode
                            
                level.append(node.val)
            BFS.append(level)
            count +=1
        return(root)
                        
                        
                        
                        