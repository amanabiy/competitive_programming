class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        seen = Counter(["".join(sorted(i)) for i in startWords])
        ans = 0

        for w in targetWords:
            word = list(sorted(w))
            for i in range(len(word)):
                n = "".join(word[:i] + word[i+1:])
                if n in seen:
                    ans += 1
                    break
        
        return ans