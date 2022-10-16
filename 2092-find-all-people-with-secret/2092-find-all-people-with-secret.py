class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        heap = []
        gotSecret = {0: -1}
        meeting = defaultdict(list)
        meeting[0].append((firstPerson, 0))

        for x, y, time in meetings:
            meeting[x].append((y, time))
            meeting[y].append((x, time))
        
        heap.append((-1,0))
        # print(meeting)
        while heap:
            parentTime, node = heapq.heappop(heap)
            
            for person, time in meeting[node]:
                if time >= parentTime and ((person not in gotSecret) or (person in gotSecret and time < gotSecret[person])):
                    gotSecret[person] = time
                    heapq.heappush(heap, (time, person))
                    
            # print(heap, gotSecret)
        return gotSecret.keys()