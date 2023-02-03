class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefixSum = [0]
        for i in w:
            self.prefixSum.append(self.prefixSum[-1] + i)
        

    def pickIndex(self) -> int:
        picked = random.randint(1, self.prefixSum[-1])
        index = bisect.bisect_left(self.prefixSum, picked)
        return index - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()