# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inOrderList = []
        def inOrder(root):
            if root == None:
                return None
            inOrder(root.left)
            inOrderList.append(root.val)
            inOrder(root.right)
            return inOrderList
        return inOrder(root)
                
