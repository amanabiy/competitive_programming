class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        If time doesn't reach process from the earlier
        and if still doesn't reach change time to current and add to the heap an
        """
        ans = []
        heap = []
        t = 0
        currIndex = 0
        tasks = [ (time, val, i) for i, (time, val) in enumerate(tasks)]
        tasks.append((float('inf'), float('inf'), float('inf')))
        
        n = len(tasks)
        tasks.sort()
        while currIndex < n:
            time, val, i = tasks[currIndex]

            # process from the heap until in the time doesn't reach now
            while heap and t < time:
                v, index, processTime = heappop(heap)
                t += v
                ans.append(index)
                
            # push to heap if under the time
            if t < time:
                t = time
            
            heapq.heappush(heap, (val, i, time))
            currIndex += 1
            # push your current element to heap
        
        return ans