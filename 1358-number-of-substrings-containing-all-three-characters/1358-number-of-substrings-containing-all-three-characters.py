class Solution:
    def numberOfSubstrings(self, str1: str) -> int:
        seen = set()
        lastSeenIndex = defaultdict(lambda: -1)
        numSubstring = 0
        left = 0

        for right in range(len(str1)):
            lastSeenIndex[str1[right]] = right
            seen.add(str1[right])

            # shrink my window
            while len(seen) == 3:
                numSubstring += (len(str1) - right)
                if lastSeenIndex[str1[left]] == left:
                    seen.remove(str1[left])
                left += 1

        return numSubstring