class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        pops =  ['.', '.']
        while i < len(path):
            s = []
            while i < len(path) and path[i] != '/':
                s.append(path[i])
                i += 1
            if s == pops:
                if stack:
                    stack.pop()
                continue
            if  s != ['.'] and s:
                stack.append(s)
            i += 1
        ans = "/" + "/".join(["".join(i) for i in stack])
        return ans