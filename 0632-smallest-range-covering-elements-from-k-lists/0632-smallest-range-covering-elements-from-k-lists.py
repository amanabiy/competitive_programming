class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minHeap = []
        globalAns = [inf, -inf]
        ans = [inf, -inf]
        
        # add all the first once 
        for i in range(len(nums)):
            j = 0
            if len(minHeap) != len(nums):
                heapq.heappush(minHeap, (nums[i][j], i, j))
                ans[0] = min(ans[0], nums[i][j])
                ans[1] = max(ans[1], nums[i][j])
            
        globalAns = ans[::]
        while True:
            val, row, col = heapq.heappop(minHeap)
            col += 1
            if col == len(nums[row]):
                break
            newVal = nums[row][col]
            heapq.heappush(minHeap, (newVal, row, col))
            ans[1] = max(ans[1], newVal)
            ans[0] = minHeap[0][0]
            one = ans[1] - ans[0]
            two = globalAns[1] - globalAns[0]
            if one < two or (ans[0] < globalAns[0] and one == two):
                globalAns = ans[::]
        
        return globalAns
            
        