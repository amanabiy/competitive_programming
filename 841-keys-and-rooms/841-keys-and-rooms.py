class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
                     0 
                 1       3
            3   0  1   2
                
        """
        visited = [0 for i in range(len(rooms))]
        
        queue = deque(rooms[0])
        visited[0] = 1
        for key in rooms[0]:
            visited[key] = 1
            
        while queue:
            for _ in range(len(queue)):
                room = queue.popleft()
                for key in rooms[room]:
                    if not visited[key]:
                        queue.append(key)
                        visited[key] = 1
        # print(visited)
        return all(visited)
        