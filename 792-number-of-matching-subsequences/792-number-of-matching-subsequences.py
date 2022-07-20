class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        """
        Using dictionary
        """
        sub_words = defaultdict(list)
        count = 0
        
        for word in words:
            sub_words[word[0]].append(word[1:])
        
        for l in s:
            words_ = sub_words[l]
            sub_words[l] = []
            for w in words_:
                if w:
                    sub_words[w[0]].append(w[1:])
                else:
                    count += 1
        
        return count
        