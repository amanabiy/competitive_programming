class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        currCapacity = capacity

        for i in range(0, len(plants)):
            if currCapacity < plants[i]:
                steps += ((i) * 2)
                currCapacity = capacity
            steps += 1
            currCapacity -= plants[i]
        
        return steps