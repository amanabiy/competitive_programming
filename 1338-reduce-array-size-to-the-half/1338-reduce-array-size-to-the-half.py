class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        ans = 0
        
        for index, value in enumerate(sorted(count.values(), reverse=True)):
            ans += value
            if ans >= len(arr) // 2:
                return index + 1
        
        