class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        1 
        3, 1
        """
        count = 0
        i = 0
        
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        while truckSize > 0 and i < len(boxTypes):
            num, sizes = boxTypes[i][0], boxTypes[i][1]
        
            if num <= truckSize:
                count += num * sizes
            else:
                count += truckSize * sizes
            
            truckSize -= num
            i += 1
            
            
        return count
            