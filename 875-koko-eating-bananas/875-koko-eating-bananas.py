class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eatKBanana(k):
            ans = 0
            for banana in piles:
                ans += math.ceil(banana / k)
            return ans
        
        left = 1
        right = max(piles)
        ans = float('inf')
    
        while left <= right:
            mid = left + (right - left) // 2
            curr = eatKBanana(mid)
            if curr <= h and mid < ans:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans