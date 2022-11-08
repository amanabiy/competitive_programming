class Solution:
    def reverseVowels(self, s: str) -> str:
        string = list(s)
        vowels = {"a", "e", "o", "u", "i", "A", "E", "O", "U", "I"}
        left = 0
        right = len(string) - 1
        
        while left < right:
            if string[left] not in vowels:
                left += 1

            if string[right] not in vowels:
                right -= 1
            
            if string[left] in vowels and string[right] in vowels:
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1
        
        return "".join(string)