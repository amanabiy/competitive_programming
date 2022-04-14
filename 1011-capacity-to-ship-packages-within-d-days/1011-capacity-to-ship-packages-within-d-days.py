class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        """
        total_weight = sum(weights)
        left = max(weights)
        right = total_weight
        ans = float(inf)
        day = 0
        
        
        def numDays(curr_weight):
            val = 0
            day = 0
            for weight in weights:
                if val +weight > curr_weight:
                    day += 1
                    val = 0
                val += weight

            
            return day+1
            
        while left <= right:
            mid = left + (right - left) // 2

            day = numDays(mid)
            if day <= days:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
                
        return ans