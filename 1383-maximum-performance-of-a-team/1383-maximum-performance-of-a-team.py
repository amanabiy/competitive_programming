class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        efficiencySpeed = []
        taken = []
        totalSum = 0
        bestPerformance = 0
        n = len(speed)
        mod = 10 ** 9 + 7

        for i in range(n):
            efficiencySpeed.append((efficiency[i], speed[i])) # [effficency, speed]

        efficiencySpeed.sort()

        for i in range(n - 1, -1, -1):
            while len(taken) == k:
                totalSum -= heapq.heappop(taken)
            totalSum += efficiencySpeed[i][1]
            heapq.heappush(taken, efficiencySpeed[i][1])
            bestPerformance = max(bestPerformance, (totalSum * efficiencySpeed[i][0]) )
        
        return bestPerformance % mod