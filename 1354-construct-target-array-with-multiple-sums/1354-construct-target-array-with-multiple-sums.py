class Solution:
    def isPossible(self, target: List[int]) -> bool:
        """
        n 1's
        and then replace
        [9, 3, 5]
        [1, 3, 5]
        [1, 3, 1]
        [1, 1, 1]
        
        [1, 1, 1, 2]
        [1, 1, 1, 1]
        
        [8, 5]
        [3, 5]
        [3, 2]
        [1, 2]
        [1, 1]
        """
        if len(target) == 1:
            return target[0] == 1

        target = [-i for i in target]
        heapq.heapify(target)
        total_sum = sum(target)

        while True:
            num1 = heapq.heappop(target)
            total_sum -= num1
            
            n = max(((num1 + 1) // total_sum), 1)
            diff = num1 - (total_sum * n)

            if num1 == -1:
                return True
            
            if -diff <= 0:
                return False
    
            heapq.heappush(target, diff)
            total_sum += diff
            
            