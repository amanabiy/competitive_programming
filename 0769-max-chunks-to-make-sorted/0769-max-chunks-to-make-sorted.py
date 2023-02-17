class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        lastPos = arr[0]
        
        for i in range(len(arr)):
            lastPos = max(lastPos, arr[i])
            if lastPos == i:
                chunks += 1
        
        return chunks