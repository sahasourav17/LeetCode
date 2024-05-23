# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
- If we encounter a node which is greater than high then we
  try to traverse to left bcoz, there will be nodes greater
  than high so there is no use.

- If we encounter a node which is lesser than low then we
  try to traverse to right bcoz, there will be nodes lesser
  than low so there is no use. 
'''
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
