class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def isPossibeInNDays(n):
            count = 0
            left = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= n:
                    if i - left + 1 == k:
                        count += 1
                        left = i + 1
                        
                else:
                    left = i + 1
            
            return count >= m
        
        left = 0
        right = 10 ** 9
        ans = float('inf')

        while left <= right:
            mid = left + (right - left) // 2
            if isPossibeInNDays(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans if ans != float('inf') else -1