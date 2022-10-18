class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
         0 1 2 3 4
        [0,1,3,5,6]
         l m r
         0 1 2 3 4
        [0,0,0,0,0]
                    l
                 m
                 r
         5 - 2 -> 3 <= 0 -> false
         5 - 3 -> 2 <= 0 -> false
         5 - 4 -> 1 <= 0 -> false
         
         
        """
        
        left = 0
        numCitations = len(citations)
        right = numCitations - 1
        ans = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if numCitations - mid <= citations[mid]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return numCitations - ans if ans != -1 else 0