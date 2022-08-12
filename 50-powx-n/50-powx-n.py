class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        if n == 0:
            return 1

        mul = self.myPow(x, n // 2)

        return mul * mul * x if n % 2 else mul * mul
            