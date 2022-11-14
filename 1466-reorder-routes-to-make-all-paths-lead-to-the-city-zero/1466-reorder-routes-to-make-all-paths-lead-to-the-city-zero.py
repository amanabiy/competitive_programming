class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        incoming:
        0: 4
        3: 2
        
        outgoingEdges:
        0: 1
        1: 3
        2: 3
        4: 0, 5
        
        reversedEdges = 0 + 1 + 1 + 1
        0 -> 
            1 -> 
              3 ->
                2 ->
                  None
            4 -> 
              5 -> 
                None

        
        Time: O(edges) -> edges is the number of edges I have
        Space: O(n) -> the number of cities there
        n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
        incoming:
            0: 1
            2: 1, 3
            4: 3
         
        outgoing:
            1: 0, 2
            3: 2, 4
        
        queue = [4]
        rev = 2
        """
        incomingGraph = defaultdict(list)
        outgoingGraph = defaultdict(list)
        queue = deque([0])
        visited = set([0])
        reversedEdges = 0

        for A, B in connections:
            incomingGraph[B].append(A)
            outgoingGraph[A].append(B)

        while queue:
            node = queue.popleft()
            
            # add to queue from the incoming Graph
            for city in incomingGraph[node]:
                if city not in visited:
                    visited.add(city)
                    queue.append(city)
            
            # add to queue and consider this path to be reversed
            for city in outgoingGraph[node]:
                if city not in visited:
                    visited.add(city)
                    queue.append(city)
                    reversedEdges += 1
        
        return reversedEdges
        