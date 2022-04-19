class Solution:
    def countVowels(self, word: str) -> int:
        prev = 0
        ans = 0
        vowels = set(['a', 'e', 'i', 'o','u'])
        for i in range(len(word) - 1, -1, -1):
            if word[i] in vowels:
                prev += (len(word) - i)
            ans += prev
            
        return ans