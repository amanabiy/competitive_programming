class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        a = [c for c in count.values()]
        n = len(a)
        col = 0
        v = 0
        a.sort()

        for i in range(n - 1, -1, -1):
            col += a[i]
            v += 1
            if col >= len(arr) // 2:
                break
        
        return v