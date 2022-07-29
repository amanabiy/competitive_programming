class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        
        for word in words:
            map_to_pattern = defaultdict(str)
            map_to_word = defaultdict(str)
            visited = set()
            is_matched = True
            
            for i in range(len(word)):
                if word[i] in map_to_word and map_to_word[word[i]] != pattern[i] or \
                   pattern[i] in map_to_pattern and map_to_pattern[pattern[i]] != word[i]:
                    is_matched = False
                    break
            
                map_to_word[word[i]] = pattern[i]
                map_to_pattern[pattern[i]] = word[i]
            
            if is_matched:
                ans.append(word)
        
        return ans