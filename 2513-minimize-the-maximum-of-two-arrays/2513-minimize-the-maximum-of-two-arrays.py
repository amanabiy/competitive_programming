class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        left = 1
        right = 10**10
        LCM = lcm(divisor1, divisor2)
        
        while left < right:
            # take a mid
            mid = left + (right - left) // 2
            
            divByBoth = mid // LCM
            divBy1 = mid // divisor1
            divBy2 = mid // divisor2
            
            remCount1 = max(uniqueCnt1 - divBy2 + divByBoth, 0)
            remCount2 = max(uniqueCnt2 - divBy1 + divByBoth, 0)
            total = (mid - divBy1 - divBy2 + divByBoth)
            
            # consider the mid to be an answer shrink
            if total >= remCount1 + remCount2:
                right = mid
            # expand
            else:
                left = mid + 1

        return left
            