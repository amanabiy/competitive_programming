class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
            minHeap = nums[::]
            heapify(minHeap)
            ans = 0

            while minHeap:
                val = heappop(minHeap)
                if val == 0:
                    continue

                while minHeap and val == minHeap[0]:
                    heappop(minHeap)
                
                ans += 1
                for i in range(len(minHeap)):
                    minHeap[i] -= val

            return ans