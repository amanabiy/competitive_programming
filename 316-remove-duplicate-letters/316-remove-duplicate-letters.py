class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        pos = {}
        stack = []
        visited = set()
        
        for i in range(len(s)):
            pos[s[i]] = i
        
        for i in range(len(s)):
            while s[i] not in visited and stack and \
            pos[s[stack[-1]]] > i and s[i] < s[stack[-1]]:
                visited.remove(s[stack.pop()])
            if s[i] not in visited:
                visited.add(s[i])
                stack.append(i)

        return "".join([s[i] for i in stack])
                