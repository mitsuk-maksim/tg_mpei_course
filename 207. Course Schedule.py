# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = [[] for _ in range(numCourses)]
        degree = [0 for _ in range(numCourses)]

        for course, pre in prerequisites:
            G[pre].append(course)
            degree[course] += 1

        zero_degree = [_ for _ in range(numCourses) if degree[_] == 0]

        if len(zero_degree) == 0:
            return False

        for i in zero_degree:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    zero_degree.append(j)

        return len(zero_degree) == numCourses
