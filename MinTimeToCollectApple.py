class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
            Construct the trees
            as the tree is undirected, this can be think as a graph
        """

        tree = defaultdict(list)
        for u,v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        def dfs(currentNode,parentNode):
            totalTime = 0
            for neighbor in tree[currentNode]:
                if neighbor != parentNode:
                    totalTime += dfs(neighbor,currentNode)
            
            # Case 1: If totalTime != 0, found apples
            # Case 2: hasApple[currentNode] == True , found apples
            # for both cases we have to add 2 to  the totalTime 
            if totalTime or hasApple[currentNode]:
                return totalTime + 2
            
            return totalTime
        
        # subtract 2 as we are adding extra 2 for coming back to node 0
        return max(dfs(0,-1)-2,0)

