from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # print(graph)

        vis = set()

        def dfs(src,dest):
            if src == dest:
                return True
            vis.add(src)

            for v in graph[src]:
                if v not in vis:
                    if dfs(v,dest):
                        return True
            return False

        return dfs(source,destination)