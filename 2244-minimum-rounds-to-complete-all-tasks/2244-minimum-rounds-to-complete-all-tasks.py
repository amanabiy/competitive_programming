class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        ans = 0
        
        for key in count:
            x = count[key]
            y = float('inf')
            if x == 1:
                return -1
            if x % 3 == 0:
                ans += x // 3
            else:
                ans += x // 3 + 1

        return ans