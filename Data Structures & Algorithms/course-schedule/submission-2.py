class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}

        for i in range(numCourses):
            adjList[i] = []
        
        for course, preReq in prerequisites:
            adjList[course].append(preReq)
        
        visited = set()

        def canGet(course):
            if course in visited:
                return False
            
            if adjList[course] == []:
                return True
                        
            visited.add(course)

            for pre in adjList[course]:
                if not canGet(pre):
                    return False
            
            visited.remove(course)
            adjList[course] = []

            return True
        
        ##For every course that has preReq(s), dfs over each one and make sure each is doable

        for c in range(numCourses):
            if not canGet(c):
                return False
        
        return True

        

        