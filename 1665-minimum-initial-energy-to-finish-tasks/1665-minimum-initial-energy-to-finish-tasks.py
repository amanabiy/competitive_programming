class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: [x[1] - x[0]], reverse=True)
        ans = 0
        profit = 0
        
        # print(tasks)
        for value, minimum in tasks:
            # if p
            if profit:
                minimum = max(0, minimum - profit)
                value, profit = max(value - profit, 0), max(0, profit - value)
            ans += max([0, minimum, minimum - value, value])
            profit += max(0, minimum - value)
            # print(ans, profit)
        
        return ans