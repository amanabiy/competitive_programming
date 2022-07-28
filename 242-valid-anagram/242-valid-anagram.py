class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_letters_str = Counter(s)
        count_letters_anagram = Counter(t)
        return count_letters_anagram == count_letters_str