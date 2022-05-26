class Solution:
    def arrangeWords(self, text: str) -> str:
        words = defaultdict(list)
        ans = []
        
        for word in text.split(" "):
            if word[0].isupper():
                word = chr(ord(word[0]) + 32) + word[1:]
            words[len(word)].append(word)

        
        for i in sorted(words.keys()):
            ans += words[i]

        if not ans[0][0].isupper():
            ans[0] = chr(ord(ans[0][0]) - 32) + ans[0][1:]
        
        return " ".join(ans)