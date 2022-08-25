class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = Counter(magazine)
        
        for l in ransomNote:
            if not letters[l]:
                return False
            letters[l] -= 1

        return True