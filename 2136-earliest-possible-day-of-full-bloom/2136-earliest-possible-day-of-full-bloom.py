class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        """
        plantTime = [1,3,4], 
        growTime = [2,1,3]
        
        """
        totalTime = 0
        maxTime = 0
        plants = []
        
        for i in range(len(plantTime)):
            plants.append((growTime[i], plantTime[i]))
        
        plants.sort(reverse=True)
        
        for g, p in plants:
            maxTime = max(totalTime + p + g, maxTime)
            totalTime += p
            
        return maxTime
            