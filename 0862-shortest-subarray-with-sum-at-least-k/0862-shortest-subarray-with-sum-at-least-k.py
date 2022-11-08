class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        nums = [2,-1,2], k = 4
                |
                3 -> the least number I could get is 
               [1, 2, -1, 2, 3, 4]
                1  3      4    
                3 1 
               [1,1,1,1]
                1 2 3 4

        at each point there are subbarray I can combine this with 
        
        """
        queue = deque([])
        prefixSum = [0]
        ans = float('inf')
        
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)
    
        for i in range(len(nums) + 1):
            
            while queue and prefixSum[i] - prefixSum[queue[0]] >= k:
                ans = min(ans, i - queue.popleft())
            
            while queue and prefixSum[queue[-1]] >= prefixSum[i]:
                queue.pop()

            queue.append(i)            
        
        return -1 if ans == float('inf') else ans
               
            