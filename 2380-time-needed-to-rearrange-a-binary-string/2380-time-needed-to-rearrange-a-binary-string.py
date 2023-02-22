class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        """
        "001011"
        010101
        101010
        110100
        111000
        """
        time = 0
        s = list(s)
        swap = True
        toSwap = deque()
        
        for i in range(len(s) - 1):
            if s[i] == "0" and s[i + 1] == "1":
                toSwap.append(i)

        while toSwap:
            nextLevel = deque()
            for j in range(len(toSwap)):
                i = toSwap.pop()
                s[i], s[i + 1] = s[i + 1], s[i]
                if i + 2 < len(s) and s[i + 2] == "1":
                    nextLevel.appendleft(i + 1)
                if i > 0 and s[i - 1] == "0":
                    nextLevel.appendleft(i - 1)
    
            time += 1
            toSwap = nextLevel
        
        return time
        
        