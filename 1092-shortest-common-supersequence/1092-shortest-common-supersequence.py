class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # build the common subsequence dp
        dp = [[0 for _ in range(len(str2) + 1)] for i in range(len(str1) + 1)]
        
        # fill the dp
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])

        # get the common subsequences occurence
        ans = []
        i = len(str1)
        j = len(str2)
        while i > 0 or j > 0:
            if i > 0 and dp[i][j] == dp[i - 1][j]:
                ans.append(str1[i - 1])
                i -= 1
            elif j > 0 and dp[i][j] == dp[i][j - 1]:
                ans.append(str2[j - 1])
                j -= 1
            else:
                ans.append(str1[i - 1])
                i -= 1
                j -= 1

        return ''.join(reversed(ans))