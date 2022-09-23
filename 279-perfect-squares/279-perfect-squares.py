class Solution {
public:
    int numSquares(int n) {
        vector<int>coins;
        for (int i = 1; i * i <= n; i++) {
            coins.push_back(i*i);
        }
        vector<int>dp(n + 1,1e9);
        dp[0] = 0;
        for (int i = 0; i <=n ;i++) {
            for (auto c: coins)
                if (i >= c)
                    dp[i] = min(dp[i], dp[i - c] + 1);
        }
        return dp[n];
    }
};