class Solution:
    def expandEnd(self, s, startIndex, last, visited):
        end = last[s[startIndex]]
        for i in range(startIndex, len(s)):
            if i > end:
                break
            if s[i] in visited:
                return -1
            end = max(last[s[i]], end)

        return end
    
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        last = {}
        seen = set()
        ans = []

        # get the last position of the letters
        for i, l in enumerate(s):
            last[l] = i
        end = float('-inf')

        # Iterate and try to expand
        for i in range(len(s)):
            lastInd = self.expandEnd(s, i, last, seen)
            # consider whether to add it to ans or just replace the previous one                
            if lastInd != -1:
                if end < i:
                    ans.append(s[i:lastInd + 1])
                elif lastInd <= end:
                    ans[-1] = s[i:lastInd + 1]
                end = lastInd
            seen.add(s[i])

        return ans
