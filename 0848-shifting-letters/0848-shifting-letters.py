class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shiftSum = [0] * (len(s) + 1)
        
        for i in range(len(shifts) - 1, -1, -1):
            shiftSum[i] += shiftSum[i + 1] + shifts[i]
        
        shiftSum = [ i % 26 for i in shiftSum ]
        
        ans = []

        for i, ch in enumerate(s):
            newChar = ord(ch) + shiftSum[i]
            if newChar > ord('z'):
                newChar = newChar - ord('z') + ord('a') - 1
            ans.append(chr(newChar))
        
        return ''.join(ans)