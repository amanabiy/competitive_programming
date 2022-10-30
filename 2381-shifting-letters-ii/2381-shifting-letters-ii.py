class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        """
        
        """
        shiftSum = [0] * (len(s) + 1)
        ans = []

        # create the cumulative sum
        for left, right, val in shifts:
            right += 1
            if val:
                shiftSum[left] += 1
                shiftSum[right] -= 1
            else:
                shiftSum[left] -= 1
                shiftSum[right] += 1
        
        currSum = 0
        for i, ch in enumerate(s):
            currSum += shiftSum[i]
            currChar = ((ord(s[i]) - 97 + currSum) % 26) + 97
            ans.append(chr(currChar))
        
        return ''.join(ans)
        