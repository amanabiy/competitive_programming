class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        w1 = 0
        w2 = 0 
        ans = []
        while w1 < len(word1) or w2 < len(word2):
            if word1[w1:] > word2[w2:]:
                ans.append(word1[w1])
                w1 += 1
            else:
                ans.append(word2[w2])
                w2 += 1
        return "".join(ans)
