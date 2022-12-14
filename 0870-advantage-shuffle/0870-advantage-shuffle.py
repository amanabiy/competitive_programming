class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        heap1 = []
        heap2 = []
        n = len(nums1)
        ans = [-1] * n

        for i in range(n):
            heapq.heappush(heap1, (-nums1[i], i))
            heapq.heappush(heap2, (-nums2[i], i))
        
        while heap2:
            val, i = heapq.heappop(heap2)
            val *= -1
            if val < heap1[0][0] * -1:
                v, _ = heapq.heappop(heap1)
                ans[i] = v * -1
        
        for i in range(n):
            if ans[i] == -1:
                ans[i] = heapq.heappop(heap1)[0] * -1
        
        return ans
        