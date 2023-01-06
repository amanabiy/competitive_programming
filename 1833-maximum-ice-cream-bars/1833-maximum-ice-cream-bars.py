class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        price = 0
        
        for i in range(len(costs)):
            price += costs[i]
            if price > coins:
                return i
            
        return len(costs)