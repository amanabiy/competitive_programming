class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        allInCityA = sum([i for i, j in costs])
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs)

        for i in range(n - 1, n // 2 - 1, -1):
            allInCityA -= costs[i][0]
            allInCityA += costs[i][1]

        return allInCityA