class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        color = [0] * numCourses # 0 not seen, 1 on the current path, 2 finished processing
        orderedCourses = []
        coursesPre = defaultdict(list)
        
        # build graph
        for c, prerequisite in prerequisites:
            # finish prerequisite to do course c
            coursesPre[prerequisite].append(c)
        
        def dfsAndisCycle(node):
            if color[node] == 1:
                return True
            if color[node] == 2:
                return False
            
            # mark your current node in current path
            color[node] = 1
            
            for neigh in coursesPre[node]:
                if dfsAndisCycle(neigh):
                    return True
            
            # mark it as completed and retun no cycle found
            color[node] = 2
            orderedCourses.append(node)
            return False
        
        
        # iterate and do dfs
        for i in range(numCourses):
            if dfsAndisCycle(i):
                return []
        
        return reversed(orderedCourses)
        