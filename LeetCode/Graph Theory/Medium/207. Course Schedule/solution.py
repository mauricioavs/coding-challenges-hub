# Complexity:
# Time: O(V + E): We visit each course (vertex) and each prerequisite relationship (edge) once.
# Space: O(V + E): The graph representation takes O(V + E) space,
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False
            
            if state[course] == 2:
                return True

            state[course] =  1

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            state[course] = 2

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            
        