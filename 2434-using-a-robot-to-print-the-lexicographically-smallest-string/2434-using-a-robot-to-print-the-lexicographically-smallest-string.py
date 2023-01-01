class Solution:
    def robotWithString(self, s: str) -> str:
        """
        s -> "cawerbasf"
              aaaaaa a ff -> 26 * n -> 26 charcter -> bit
                     sf
        t -> cwerbs
        paper -> aa
        """
        n = len(s)
        lessInFuture = Counter(s)
        t = []
        ans = []

        # add a dummy data to remove all at the end
        s += chr(ord('z') + 1)

        # iterating and deciding whether to include it or not
        for i in range(n + 1):
            while t and ord(t[-1]) <= ord(s[i]):
                allowPop = True
                for num in range(ord('a'), ord(t[-1])):
                    if lessInFuture[chr(num)] > 0:
                        allowPop = False
                        break
                if allowPop:
                    ans.append(t.pop())
                else:
                    break
            lessInFuture[s[i]] -= 1
            t.append(s[i])

        return ''.join(ans)