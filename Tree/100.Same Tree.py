# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Base case
        if p and q and p.val != q.val:
            return False
        elif p and not q or not p and q:
            return False
        if p == None and q == None:
            return True
         
        return self.isSameTree(p.left, q.left) and  self.isSameTree(p.right, q.right)
