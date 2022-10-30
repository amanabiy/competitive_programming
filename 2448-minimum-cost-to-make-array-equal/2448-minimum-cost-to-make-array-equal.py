class Solution:
    def getMinCostRightToLeft(self, numCost):
        ltf = 0
        n = len(numCost)
        prefixSum = 0

        # get cost for the lastToFirst
        for i in range(n - 1, 0, -1):
            ltf += numCost[i][1] * abs(numCost[i][0] - numCost[0][0])
            prefixSum += numCost[i][1]

        lastToFirst = [ltf]
        
        for i in range(1, n):
            # minus the distance between before and current
            lastToFirst.append(lastToFirst[-1] - ((prefixSum * abs(numCost[i - 1][0] - numCost[i][0]))))
            prefixSum -= numCost[i][1]
        
        return lastToFirst
    
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        firstToLast = [0]
        numCost = defaultdict(int)
        total = 0

        for i in range(n):
            numCost[nums[i]] += cost[i]
            total += cost[i]

        numCost = list(numCost.items())
        numCost.sort()
        left = self.getMinCostRightToLeft(numCost)
        right = self.getMinCostRightToLeft(numCost[::-1])[::-1]
        
        return min([ left[i] + right[i] for i in range(len(numCost)) ])

