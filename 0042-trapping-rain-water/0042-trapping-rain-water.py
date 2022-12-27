class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]
        right = [0]
        n = len(height)
        ans = 0

        for i in range(n):
            left.append(max(left[-1], height[i]))
            right.append(max(right[-1], height[n - 1 - i]))

        right = right[::-1]
        
        for i in range(n):
            ans += max(0, min(left[i+1], right[i]) - height[i])
        
        return ans