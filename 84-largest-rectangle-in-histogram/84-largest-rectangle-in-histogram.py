class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        [2, 1, 5, 6, 2, 3, -inf]        
         0  1  2  3  4  5    6
        [(1, 1)]  curr = (-inf, 6)
        
        (6, 3) -> (2 - 3) * 6 * (4 - 3) = 6
        (5, 2) -> (2 - 1) * 5 * (4 - 2) = 1 * 5 * 2 = 10
        (3, 5) -> (5 - 4) * 3 * (6 - 5) = 1 * 3 * 1 = 3
        (2, 4) -> (4 - 1) * 2 * (6 - 4) = 3 * 2 * 3 = 
        
        area = max(2, 6, 10, 3)
        """
        stack = []
        ans = 0
        heights.append(float('-inf'))
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >  heights[i]:
                popped = stack.pop()
                lastIndex = stack[-1] if stack else -1
                leftArea = (popped - lastIndex) * heights[popped]
                rightArea = (i - popped - 1) * heights[popped]
                # print(popped, LeftArea, RightArea, LeftArea + RightArea)
                ans = max(ans, leftArea + rightArea)
            stack.append(i)
        
        heights.pop()
        return ans
                