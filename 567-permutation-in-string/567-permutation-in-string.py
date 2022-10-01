class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        count = {a: 1, b: 1}
        """
        countS1 = Counter(s1)
        left = 0
        countCollected = defaultdict(int)
        for index, i in enumerate(s2):
            if i in countS1:
                while countCollected[i] >= countS1[i]:
                    if s2[left] in countS1:
                        countCollected[s2[left]] -= 1
                    left += 1
                countCollected[i] += 1
                # print(countCollected, left, i)
                if countCollected == countS1:
                    return True
            else:
                countCollected = defaultdict(int)
                left = index + 1
        
        return False
        