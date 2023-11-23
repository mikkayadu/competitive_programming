# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, values):
            if not root:
                return 
            
            dfs(root.left, values)
            values.append(root.val)
            dfs(root.right, values)
        
        values  = []
        dfs(root, values)
        print(values)
        sort_values = sorted(values)
        return values == sort_values  and len(set(values)) == len(values)