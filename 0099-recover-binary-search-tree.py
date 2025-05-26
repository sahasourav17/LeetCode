# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev, first_v, second_v = None, None, None

        def inorder(root):
            nonlocal prev, first_v, second_v
            if not root:
                return

            inorder(root.left)

            if prev and prev.val > root.val:
                if not first_v:
                    first_v = prev
                second_v = root

            prev = root
            inorder(root.right)

        inorder(root)

        if first_v and second_v:
            first_v.val, second_v.val = second_v.val, first_v.val

# Time Complexity: O(N)
# Space Complexity: O(1)
