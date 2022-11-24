class Solution:
    def findLongesIncreasingSubsequence(self, arr):
        ans = []
        for num in arr:
            if not ans or ans[-1] <= num:
                ans.append(num)
            else:
                left = 0
                right = len(ans) - 1
                index = bisect.bisect_right(ans, num)
                ans[index] = num
        
        return len(ans)
                
                
    def kIncreasing(self, arr: List[int], k: int) -> int:
        ans = 0
        
        
        for j in range(k):
            collect = []
            for i in range(j, len(arr), k):
                collect.append(arr[i])
            longest = self.findLongesIncreasingSubsequence(collect)
            ans += len(collect) - longest
        
        return ans