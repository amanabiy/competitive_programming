class Solution:
    def checkValidString(self, s: str) -> bool:
        openBracket = []
        unbalanced = []

        # remove balanced once
        for i, b in enumerate(s):
            if b == '(':
                openBracket.append(i)
            elif b == '*':
                unbalanced.append(i)
            else:
                if openBracket:
                    openBracket.pop()
                else:
                    unbalanced.append(i)
        
        stack = []
        unbalanced += openBracket
        unbalanced.sort()

        # balance closing brackets
        for j, b in enumerate(unbalanced):
            if s[b] == '(':
                stack.append(b)
            else:
                if stack and s[stack[-1]] != s[b]:
                    stack.pop()
                elif s[b] == '*':
                    stack.append(b)
                else:
                    print(unbalanced, stack)
                    return False
        
        # check if the remaining are not opening brackets
        for i in stack:
            if s[i] != '*':
                return False
        
        return True