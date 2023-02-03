class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefixSum = [0]
        for i in w:
            self.prefixSum.append(self.prefixSum[-1] + i)
        

    def pickIndex(self) -> int:
        picked = random.randint(1, self.prefixSum[-1])
        left = 0
        right = len(self.prefixSum) - 1
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            if self.prefixSum[mid] >= picked:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()