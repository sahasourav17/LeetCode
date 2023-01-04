# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
            Case 1: if two trees are empty
            Case 2: if they are non empty 
            Case 3: if one empty other non empty
        """
        def dfs(p,q):
            if p is None and q is None:
                return True
            if p is not None and q is not None:
                return ((p.val == q.val) and dfs(p.left,q.left) and dfs(p.right,q.right))
            return False
        return dfs(p,q)