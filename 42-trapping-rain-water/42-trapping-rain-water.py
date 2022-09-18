class Solution:
    def trap(self, height: List[int]) -> int:
        """
        whole decrease 
        when decrease -> do some operation
        when increase -> do some operation
        543213
        """
        
        n = len(height)
        prev = height[0]
        ind= 0
        water, temp = 0, 0
        for i in range(1, n):
            if (height[i] >= prev):
                prev = height[i]
                ind = i
                temp = 0
            else:
                water += prev - height[i]
                temp += prev - height[i]
        if (ind < n-1):
            water -= temp
            prev = height[-1]
            for i in range(n-1, ind - 1, -1):
                if (height[i] >= prev):
                    prev = height[i]
                else:
                    water += prev - height[i]
        return water