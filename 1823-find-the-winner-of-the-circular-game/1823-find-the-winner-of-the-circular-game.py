class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        curr = [i+1 for i in range(n)]
        i = 0

        while len(curr) > 1:
            i += k - 1
            i  %= len(curr)
            curr.pop(i)
            if i >= len(curr):
                i = 0

        return curr[0]