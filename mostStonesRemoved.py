class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row,col = defaultdict(set),defaultdict(set)

        for x,y in stones:
            row[x].add((x,y))
            col[y].add((x,y))

        vis = set()

        def dfs(u,v):
            vis.add((u,v))
            node = (row[u].union(col[v])-vis)
            for p,q in node:
                dfs(p,q)

        notRemoved = 0

        for x,y in stones:
            if (x,y) not in vis:
                dfs(x,y)
                notRemoved += 1
        return len(stones)-notRemoved