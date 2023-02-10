class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return list(sorted(map(lambda x: x * x, nums)))