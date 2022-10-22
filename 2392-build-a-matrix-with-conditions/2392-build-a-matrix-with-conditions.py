class Solution:
    def topSort(self, graph, indegree, k):
        queue = deque()
        sortedGraph = []

        for node in range(k):
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            sortedGraph.append(node)
            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        
        return sortedGraph

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        """
        1 ->           1   2   3
              2        1   3   2
        3 ->
        
        
        1 -> 
             2
        3 ->

        1 ->
             4
        3 ->

                       1   2   3   
        3 -> 2 -> 1    3   2   1
        
        """
        # intialize the variables
        rowGraph = [[] for _ in range(k)]
        colGraph = [[] for _ in range(k)]
        rowIndegree = [ 0 for _ in range(k) ]
        colIndegree = [ 0 for _ in range(k) ]
        matrix = [ [-1 for _ in range(k)]  for _ in range(k)]

        # buld graphs and count indegreees
        for up, down in rowConditions:
            rowGraph[up - 1].append(down - 1)
            rowIndegree[down - 1] += 1
        
        for left, right in colConditions:
            colGraph[left - 1].append(right - 1)
            colIndegree[right - 1] += 1
        
        # topsort the graphs
        rowTopSort = self.topSort(rowGraph, rowIndegree, k)
        colTopSort = self.topSort(colGraph, colIndegree, k)
        
        # check that I have equal number of nodes on both topsort
        # other wise there is a cycle so return []
        if len(rowTopSort) != k or len(colTopSort) != k:
            return []
        
        for i in range(k):
            for j in range(k):
                if rowTopSort[i] == colTopSort[j]:
                    matrix[i][j] = rowTopSort[i] + 1
                else:
                    matrix[i][j] = 0
        
        return matrix
        
        
        
        