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
        lessInFuture = [0] * (n + 1)
        a = ord('a')
        t = []
        ans = []
        
        # making the prefix array
        for i in range(n - 1, -1, -1):
            letter = ord(s[i]) - a
            lessInFuture[i] = lessInFuture[i + 1] | 1 << letter
        
        # add a dummy data to remove all at the end
        s += chr(ord('z') + 1)

        # iterating and deciding whether to include it or not
        for i in range(n + 1):
            while t and ord(t[-1]) <= ord(s[i]):
                allowPop = True
                for num in range(ord(t[-1]) - ord('a')):
                    if lessInFuture[i] & (1 << num):
                        allowPop = False
                        break
                if allowPop:
                    ans.append(t.pop())
                else:
                    break
            t.append(s[i])

        return ''.join(ans)