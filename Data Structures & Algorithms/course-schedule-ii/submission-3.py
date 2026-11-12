class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}

        for i in range(numCourses):
            adjList[i] = []
        
        for course, preReq in prerequisites:
            adjList[course].append(preReq)
        
        visited, path = set(), set()
        res = []

        def canGet(course):
            if course in path:
                return False
            if course in visited:
                return True
            
            path.add(course)

            for pre in adjList[course]:
                if not canGet(pre):
                    return False
            
            visited.add(course)
            path.remove(course)
            res.append(course)
            return True

        for c in range(numCourses):
            if not canGet(c):
                return []
        
        return res