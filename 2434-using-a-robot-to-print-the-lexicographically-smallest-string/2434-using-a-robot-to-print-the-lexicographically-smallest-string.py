class Solution:
    def robotWithString(self, s: str) -> str:
        """
        s -> "cawerb a sf"
              aaaaaa a ff -> 26 * n -> 26 charcter -> bit
                     sf
        t -> cwerbs
        paper -> aa
        """
        n = len(s)
        lessInFuture = ['z'] * (n + 1)
        a = ord('a')
        t = []
        ans = []

        # add a dummy data to remove all at the end
        s += chr(ord('z') + 1)
        
        # making the prefix array
        for i in range(n - 1, -1, -1):
            lessInFuture[i] = min(s[i], lessInFuture[i + 1])
        

        # iterating and deciding whether to include it or not
        for i in range(n + 1):
            while t and t[-1] <= lessInFuture[i]:
                ans.append(t.pop())
            t.append(s[i])

        return ''.join(ans)