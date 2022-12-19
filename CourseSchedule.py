class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # mapping prereq for each courses
        preReq = {i:[] for i in range(numCourses)}

        for course,preq in prerequisites:
            preReq[course].append(preq)

        vis = set()

        def dfs(course):
            if course in vis:
                return False
            if preReq[course] == []:
                return True

            vis.add(course)

            for preq in preReq[course]:
                if not dfs(preq):
                    return False
            vis.remove(course)
            preReq[course] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True