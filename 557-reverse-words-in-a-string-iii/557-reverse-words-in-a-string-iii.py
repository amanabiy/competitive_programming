class Solution:
    def reverseWord(self, i, j, arr):
        left, right = i, j
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    def reverseWords(self, s: str) -> str:
        s = list(s)
        left = 0
        for i in range(len(s)):
            if s[i] == ' ':                
                self.reverseWord(left, i - 1, s)
                left = i + 1

        self.reverseWord(left, len(s)-1, s)
        return ''.join(s)
    