class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
          5 1 5 1 
        0 1 2 2 4
        1 1 1 3 4
        """
        left = 0
        right = 0
        prev = [1, 1]
        ans = 1
        n = len(arr)
        last = arr[0]
        
        for i in range(n):                
            if arr[i] == last:
                prev = [1, 1]
                continue
            elif arr[i] < last:
                prev[0] = prev[1] + 1
                prev[1] = 1
            else:
                prev[1] = prev[0] + 1
                prev[0] = 1
            
            ans = max([ans, prev[0], prev[1]])
            last = arr[i]

        return ans