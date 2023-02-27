class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        count = Counter()
        ans = 0
        c = 0

        logs.sort()
        
        for start, end in logs:
            for j in range(start, end):
                count[j] += 1
                if count[j] > c:
                    c = count[j]
                    ans = j
        
        # print(count)
        return ans