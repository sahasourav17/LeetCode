# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        ql = deque()
        qr = deque()

        ql.appendleft(root.left)
        qr.appendleft(root.right)

        while ql and qr:
            nodeL, nodeR = ql.pop(),qr.pop()
            if not nodeL and not nodeR:
                continue
            # both node must exist
            # if exists thet must have the same value
            if not nodeL or not nodeR or nodeL.val != nodeR.val:
                return False
            
            ql.appendleft(nodeL.left)
            ql.appendleft(nodeL.right)

            qr.appendleft(nodeR.right)
            qr.appendleft(nodeR.left) 
        return not(ql or qr)