class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        seen = set()
        ans = []
        
        def isConcatenated(word, seen, start=0, index=0):
            if index == len(word):
                return word[start:index] in seen
            
            ans = False
            if word[start:index] in seen:
                # take the previous one
                ans = ans or isConcatenated(word, seen, index, index+1)
                # just keep searching
            ans = ans or isConcatenated(word, seen, start, index+1)
            return ans
                
        
        for word in words:
            if isConcatenated(word, seen):
                ans.append(word)
            seen.add(word)
        
        return ans
        