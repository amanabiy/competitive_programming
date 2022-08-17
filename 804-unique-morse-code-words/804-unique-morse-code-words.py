class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letters = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()
        ans = 0
        
        for word in words:
            new_word = []
            for i in word:
                new_word.append(letters[ord(i) - 97])
            new_word = ''.join(new_word)
            if new_word not in seen:
                seen.add(''.join(new_word))
                ans += 1
        
        return ans