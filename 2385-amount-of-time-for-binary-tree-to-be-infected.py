# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        stack = [(root,None)]
        while stack:
            n, p = stack.pop()
            if p:
                graph[p.val].append(n.val)
                graph[n.val].append(p.val)
            if n.left:
                stack.append((n.left,n))
            if n.right:
                stack.append((n.right,n))
        ans = -1
        visited = {start}
        queue = deque([start])
        while queue:
            for i in range(len(queue)):
                u = queue.popleft()
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)
            ans += 1
        return ans
        
