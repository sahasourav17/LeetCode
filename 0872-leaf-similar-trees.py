# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def find_leaf_values(root, leaf_values):
            if root is None:
                return
            if not root.left and not root.right:
                leaf_values.append(root.val)
            find_leaf_values(root.left, leaf_values)
            find_leaf_values(root.right, leaf_values)
            
        tree1_leaf_values, tree2_leaf_values = [],[]

        find_leaf_values(root1, tree1_leaf_values)
        find_leaf_values(root2, tree2_leaf_values)

        return tree2_leaf_values == tree1_leaf_values
