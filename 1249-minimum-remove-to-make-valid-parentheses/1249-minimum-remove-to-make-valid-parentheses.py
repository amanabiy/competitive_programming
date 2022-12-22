class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        ans = []
        
        for i in range(len(s)):
            l = s[i]
            if l == "(":
                stack.append(i)
                ans.append("")
            elif l == ")":
                if stack:
                    index = stack.pop()
                    ans[index] = "("
                    ans.append(")")
                else:
                    ans.append("")
            else:
                ans.append(l)

        return "".join(ans)