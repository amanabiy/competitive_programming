import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        rooms = 4
        [[2, 13], [3, 12], [7, 10], [17, 19], [18, 19]]
        currTime = 0

        heap
            0 -> 13
            1 -> 12
            2 -> 10
            3 -> 19
        countUsed
            0 -> 0
            1 -> 0
            2 -> 0
            3 -> 0

        ans = 0
        """
        heap = []
        emptyRoom = [ i for i in range(n) ]

        currTime = 0
        usedRoom = defaultdict(int)
        meetings.sort()
        # print(meetings)
        
        for i in range(len(meetings)):
            start, end = meetings[i]
            currTime = max(start, currTime)
            
            # if all the rooms are taken
            # free at least one space or all those who ended before
            while (heap and (currTime >= heap[0][0])) or not emptyRoom:
                endingTime, room = heapq.heappop(heap)
                currTime = max(currTime, endingTime)
                heapq.heappush(emptyRoom, room)
            
            # give the least number room to the newRoom
            newRoom = heapq.heappop(emptyRoom)
            usedRoom[newRoom] += 1
            heapq.heappush(heap, [max(end, currTime + (end - start)), newRoom])

        ans = list(usedRoom.keys())
        ans.sort(key=lambda x: [-usedRoom[x], x])

        return ans[0]
        
        