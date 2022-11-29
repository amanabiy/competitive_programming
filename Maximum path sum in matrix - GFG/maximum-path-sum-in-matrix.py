#User function Template for python3

class Solution:
    def maximumPath(self, N, matrix):
        # code here
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for i in range(N)] for i in range(N + 1)]
        def inBound(row, col, n, m):
            return 0 <= row < n and 0 <= col < m
        
        for i in range(N):
            for j in range(N):
                if j + 1 < N and dp[i + 1][j] < dp[i][j + 1]:
                    dp[i + 1][j] = dp[i][j + 1]
                if j - 1 > -1 and dp[i + 1][j] < dp[i][j - 1]:
                    dp[i + 1][j] = dp[i][j - 1]
                if dp[i + 1][j] < dp[i][j]:
                    dp[i + 1][j] = dp[i][j]
                dp[i + 1][j] += matrix[i][j]


        return max(dp[-1])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends