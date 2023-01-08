class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        """
        [2,1,3,5]
        2135
        135 
        21352
        1352

        2 -> found two
        
        """
        ans = 0
        minPoint = -1
        maxPoint = -1
        lastPoint = -1
        
        for i in range(len(nums)):
            # update last point
            if nums[i] < minK or nums[i] > maxK:
                lastPoint = i
            
            if nums[i] == minK:
                minPoint = i
            
            if nums[i] == maxK:
                maxPoint = i
            
            if minPoint != -1 and maxPoint != -1:
                lastSeen = min(minPoint, maxPoint)
                if lastSeen < lastPoint:
                    continue
                ans += (lastSeen - lastPoint)
        
        return ans