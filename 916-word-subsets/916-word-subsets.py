class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        Time: O(word1 + word2)
        Space: O(word1 + word2)
        """
        wordsd = defaultdict(int)
        for word in words2:
            for l in word:
                count = word.count(l)
                wordsd[l] = max(count, wordsd[l])
                    
            
        words2 = wordsd
        ans = []

        for word in words1:
            word_ = Counter(word)
            count = 0
            
            for  key in words2.keys():
                if word_[key] >= words2[key]:
                    count += 1

            if count == len(words2.keys()):
                ans.append(word)
        
        return ans