class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        smallest = float('inf')
        stack = []
        
        for num in nums:
            while stack and stack[-1][0] < num:
                stack.pop()

            if stack and stack[-1][1] < num < stack[-1][0]:
                return True
            
            stack.append((num, smallest))
            smallest = min(smallest, num)
    
        return False