class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
            minHeap=[]
            for i in nums:
                if i!=0:
                    heappush(minHeap,i)
            ans=0
            while minHeap:
                t=heappop(minHeap)
                while minHeap and t==minHeap[0]:
                    heappop(minHeap)
                ans+=1
                for i in range(len(minHeap)):
                    minHeap[i]-=t

            return ans