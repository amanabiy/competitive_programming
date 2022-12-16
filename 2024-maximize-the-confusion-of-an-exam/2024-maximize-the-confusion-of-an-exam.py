class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        falseCount = 0
        trueCount = 0
        
        left = 0
        ans = 0
        
        for i in range(len(answerKey)):
            if answerKey[i] == 'T':
                trueCount += 1
            else:
                falseCount += 1
            
            while min(falseCount, trueCount) > k:
                if answerKey[left] == 'T':
                    trueCount -= 1
                else:
                    falseCount -= 1
                left += 1
            ans = max(ans, i - left + 1)

        return ans