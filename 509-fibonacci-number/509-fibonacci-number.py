memory = {}
class Solution:
    def fib(self, n: int) -> int:
        if n in memory:
            return memory[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        memory[n] = self.fib(n-1) + self.fib(n-2)
        return memory[n]