class Solution:
    def getForwardSum(self, arr):
        value = {}
        ans = [0] * len(arr)
        
        
        for ind, val in enumerate(arr):
            if val not in value:
                value[val] = [0, 0, ind]
                continue
            lastSum, lastCount, lastInd = value[val]
            lastCount += 1
            currSum = ((ind - lastInd) * lastCount) + lastSum
            value[val] = [currSum, lastCount, ind]
            ans[ind] = currSum
        
        return ans
            
            
    def getDistances(self, arr: List[int]) -> List[int]:
        forward = self.getForwardSum(arr)
        backward = self.getForwardSum(arr[::-1])[::-1]
        return [ forward[i] + backward[i] for i in range(len(arr)) ]
        