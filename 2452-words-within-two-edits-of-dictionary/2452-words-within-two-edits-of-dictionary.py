class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        dictionaries = set()
        ans = []
        
        for word in dictionary:
            for i in range(len(word)):
                w = word[:i] + "*"
                dictionaries.add(w + word[i+1:])
                for j in range(i + 1, len(word)):
                    x = w + word[i+1:j] + "*" + word[j+1:]
                    dictionaries.add(x)

        for word in queries:
            for i in range(len(word)):
                w = word[:i] + "*"
                added = False
                if w + word[i+1:] in dictionaries:
                    ans.append(word)
                    break
                for j in range(i + 1, len(word)):
                    x = w + word[i+1:j] + "*" + word[j+1:]
                    if x in dictionaries:
                        ans.append(word)
                        added = True
                        break
                if added:
                    break
        return ans