class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(sorted(profits, reverse=True)[:k])

        projects = sorted(zip(capital, profits),key=lambda x: x[0])
        # print(f"projects: {projects}")
        available_projects = []

        while k > 0:
            while projects and projects[0][0] <= w:
                _ , profit = heapq.heappop(projects)
                heapq.heappush(available_projects, -profit)
            if available_projects:
                w -= heapq.heappop(available_projects)
            k -= 1
        return w
        
