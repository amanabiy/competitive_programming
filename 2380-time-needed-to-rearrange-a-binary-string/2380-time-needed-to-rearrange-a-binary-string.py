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
        while swap:
            swap = False
            i = 0
            while i < len(s) - 1:
                if s[i] == "0" and s[i + 1] == "1":
                    s[i], s[i + 1] = s[i + 1], s[i]
                    swap = True
                    i += 1
                i += 1
            time += 1
            # print(s)
        
        return time - 1
        
        