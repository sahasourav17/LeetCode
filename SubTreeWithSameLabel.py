class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        labelCount,ansList = defaultdict(int),[0]*n

        def dfs(curNode,parNode):
            prevNode = labelCount[labels[curNode]]
            labelCount[labels[curNode]] += 1

            for childNode in graph[curNode]:
                if childNode != parNode:
                    dfs(childNode,curNode)
            ansList[curNode] = labelCount[labels[curNode]] - prevNode
        
        dfs(0,-1)
        return ansList