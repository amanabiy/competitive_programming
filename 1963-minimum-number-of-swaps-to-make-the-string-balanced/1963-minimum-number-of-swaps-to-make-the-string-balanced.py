class Solution:
    def minSwaps(self, s: str) -> int:
        brac = list(s)
        stack = []
        left = 0
        swap = 0
        right = len(s) - 1
        
        while left < right:
            if brac[left] == '[':
                stack.append('[')
            elif stack:
                stack.pop()
            else:
                while right > 0 and brac[right] != '[':
                    right -= 1
                brac[left], brac[right] = brac[right], brac[left]
                stack.append(brac[left])
                swap += 1
            left += 1
        
        return swap