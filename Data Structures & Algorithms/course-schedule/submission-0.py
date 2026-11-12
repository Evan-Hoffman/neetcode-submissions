class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}

        # for i in range(numCourses):
        #     adjList[i] = []
        
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
            
            canTakePrereqs = True
            
            visited.add(preReq)

            for course in adjList[preReq]:
                canTakePrereqs = canTakePrereqs and canGetPrereq(course, visited)
            
            visited.remove(preReq)

            return canTakePrereqs
        
        ##For every course that has preReq(s), dfs over each one and make sure each is doable

        for course, prereqs in adjList.items():
            for preReq in prereqs:
                if not canGetPrereq(preReq, set([course])):
                    return False
        
        return True

        

        