class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for l in s:
            currVal = 1
            if stack and stack[-1][0] == l:
                currVal = stack[-1][1] + 1
            stack.append([l, currVal])
            if stack and stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
        
        return ''.join([l for l, c in stack])
            