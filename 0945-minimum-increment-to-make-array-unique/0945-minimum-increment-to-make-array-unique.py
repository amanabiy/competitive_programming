class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
        1: 2
        2: 2
        
        2 -> 3, 2 -> 1
        1 -> 1, 4 -> 3
        
        1 -> 1, 2 -> 1
        2 -> 3, 4 -> 3
        
        make sure to add in visited
        a   b 
              c d -> e
        candidates =  a + 1    e
        consider the options between the last number and the current number
        
        I don't know the next number
        """
        visited = set()
        candidates = []
        op = 0
        nums.sort(reverse=True)

        for n in nums:
            c = n
            if n not in visited:
                visited.add(n)
            else:
                k = heapq.heappop(candidates)
                c = k
                op += k - n
                visited.add(c)
            if c + 1 not in visited:
                heapq.heappush(candidates, c + 1)
        
        return op