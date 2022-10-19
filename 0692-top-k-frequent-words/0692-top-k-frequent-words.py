class countName:
    def __init__(self, count, name):
        self.count = count
        self.name = name
    
    def __lt__(self, countName2):
        if self.count < countName2.count:
            return True
        elif self.count == countName2.count:
            return self.name > countName2.name
        return False

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        kWords = []
        
        count = Counter(words)
        
        for key in count:
            word = countName(count[key], key)
            heapq.heappush(kWords, word)
            if len(kWords) > k:
                heapq.heappop(kWords)
        
        ans = []
        while kWords:
            ans.append(heapq.heappop(kWords).name)
        
        return reversed(ans)