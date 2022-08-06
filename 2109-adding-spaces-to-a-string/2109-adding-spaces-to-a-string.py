class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_str = []
        j = 0
        i = 0
        
        while i < len(s):
            if j < len(spaces) and i == spaces[j]:
                new_str.append(' ')
                j += 1
            new_str.append(s[i])
            i += 1
    
        return ''.join(new_str)
            