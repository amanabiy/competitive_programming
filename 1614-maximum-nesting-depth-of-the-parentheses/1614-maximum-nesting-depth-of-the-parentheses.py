class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ans = 0
        
        for l in s:
            if l == '(':
                last = stack[-1] + 1 if stack else 1
                stack.append(last)
            elif l == ')':
                ans = max(ans, stack.pop())
        
        return ans