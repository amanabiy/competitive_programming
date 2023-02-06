class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        
        currLength = 0
        space = 0
        selected = []
        for word in words:
            if currLength + space + 1 + len(word) > maxWidth and currLength + space != 0:
                remaining = maxWidth - currLength - space
                rem = remaining % space if space else remaining
                sentence = ""
                last = selected[-1]
                selected.pop()
                for w in selected:
                    add = ""
                    if rem > 0:
                        add = " "
                        rem -= 1
                    sentence += w + add + " " * ((remaining // space) + 1)
                sentence += last + " " * rem
                ans.append(sentence)
                currLength = 0
                space = 0
                selected = []

            # if currLength + space + len(word) <= maxWidth:
            if selected:
                space += 1
            currLength += len(word)
            selected.append(word)

        text = " ".join(selected)
        if selected:
            ans.append(text + " " * (maxWidth - len(text)))
        
        return ans