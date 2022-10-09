# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([(root, root.val, [root.val])])
        
        ans = []
        
        while q:

            for i in range(len(q)):
                
                node, nval, ls = q.popleft()
                print(nval)
                if node:
                    if node.left:
                        q.append([node.left, (nval + node.left.val), ls + [node.left.val]])
                        
                        
                    if node.right:
                        q.append([node.right, (nval + node.right.val), ls + [node.right.val]])
                        
                    if not node.left and not node.right and nval==targetSum:
                        ans.append(ls)
        return(ans)