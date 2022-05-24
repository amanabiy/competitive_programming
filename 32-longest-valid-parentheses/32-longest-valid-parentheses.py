class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        dp = [0] * len(s)
        count = 0
        validUntil = 0
        countBack = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append((s[i], i))
            else:
                if stack:
                    val, idx = stack.pop()
                    dp[idx] += 1
                    dp[i] = 1
                    validUntil += 1
                else:
                    validUntil = 0
        # print(dp)
        i = 0
        ans = 0
        c = 0
        while i < len(s):
            if dp[i]:
                c = max(c, c + 1)
            else:
                ans = max(ans, c)
                c = 0
            i += 1
            # print(ans, c)
        return max(ans,c)
                
        # return ans