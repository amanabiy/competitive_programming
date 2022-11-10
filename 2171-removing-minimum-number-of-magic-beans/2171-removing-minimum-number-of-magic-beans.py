class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        [1, 2, 3, 6]
        []
        beans.sort()
        changeCost = 0
        n = len(beans)
        prefixSum = 0
        
        for i in range(1, n):
            changeCost += beans[i] - beans[0]
            prefixSum += beans[i]
        
        minCost = changeCost
        
        for i in range(1, n):
            # remove the previous one
            changeCost += beans[i - 1]
            
            # remove the cost of changing everything to the previous
            changeCost -= ((beans[i] - beans[i - 1]) * (n - i))
            minCost = min(minCost, changeCost)
        
        return minCost