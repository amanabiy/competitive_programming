class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        left = 0
        ans = set()

        for right in range(9, len(s)):
            currDNA = s[left:right+1]
            if currDNA in seen:
                ans.add(currDNA)
            seen.add(currDNA)
            left += 1
        
        return list(ans)
            
            