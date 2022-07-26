class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        queue = deque()
        visited = set()
        queue.append(start)
        countOperations = 0
        
        while queue:
            for i in range(len(queue)):
                num = queue.popleft()
                
                if num == goal:
                    return countOperations
                
                if num not in visited and 0 <= num <= 1000:
                    for i in nums:
                        queue.append(num + i)
                        queue.append(num - i)
                        queue.append(num ^ i)
                
                visited.add(num)
                
            countOperations += 1
        
        return -1