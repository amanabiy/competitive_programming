class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda a: [abs(a - x), a])
        ans = arr[:k]
        ans.sort()
        return ans