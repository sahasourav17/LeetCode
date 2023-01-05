# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postOrderList = []
        def postOrder(root):
            if root == None:
                return None
                
            postOrder(root.left)
            postOrder(root.right)
            postOrderList.append(root.val)

            return postOrderList
        return postOrder(root)