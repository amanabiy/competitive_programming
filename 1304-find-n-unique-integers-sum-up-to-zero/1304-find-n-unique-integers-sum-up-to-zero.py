class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        
        if n % 2 == 1:
            ans.append(0)
            n -= 1
        
        n //= 2
        ans += [i for i in range(-1, -1 - n, -1)]
        ans += [i for i in range(1, 1 + n, 1)]
        
        return ans