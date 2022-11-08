class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            add = True
            if stack and stack[-1].lower() == s[i].lower():
                if (stack[-1].isupper() and s[i].islower()) or \
                   (stack[-1].islower() and s[i].isupper()):
                    stack.pop()
                    add = False

            if add:
                stack.append(s[i])
        
        return ''.join(stack)