class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        
        for course, preReq in prerequisites:
            if course not in adjList:
                adjList[course] = [preReq]
            else:
                adjList[course].append(preReq)

        def canGetPrereq(preReq, visited):
            if preReq in visited:
                return False
            
            if preReq not in adjList:
                return True
                        
            visited.add(preReq)

            for course in adjList[preReq]:
                if not canGetPrereq(course, visited):
                    return False
            
            visited.remove(preReq)
            adjList[preReq] = []

            return True
        
        ##For every course that has preReq(s), dfs over each one and make sure each is doable

        for course, prereqs in adjList.items():
            for preReq in prereqs:
                if not canGetPrereq(preReq, set([course])):
                    return False
        
        return True

        

        