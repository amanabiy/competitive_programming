class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
                   
        heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
                           |
                  [0,1,2,3,4,5,6,10]  ->
                  
                  [5,3]
                  
                  so the thing is I want to use bricks for the small heights
                  and I want to use ladders for the longer heights
                  
                  I will keep using ladder until I exhaust it and then I will use brick for those which are small because it would be e                   efficient to use brick for the smaller once and ladder for the large once
                  1,1,1,1,1,4
                  1,1,1,1,1,
        """
        
        usedLaddersHeap = []
        
        for i in range(len(heights) - 1):
            if heights[i] > heights[i + 1]:
                continue

            diff =  heights[i + 1] -  heights[i]
            heapq.heappush(usedLaddersHeap, diff)
            
            if ladders:
                ladders -= 1
            else:
                theLeastDiff = heapq.heappop(usedLaddersHeap)
                
                if bricks >= theLeastDiff:
                    bricks -= theLeastDiff
                else:
                    return i
        
        return len(heights) - 1
                
                
                    
                