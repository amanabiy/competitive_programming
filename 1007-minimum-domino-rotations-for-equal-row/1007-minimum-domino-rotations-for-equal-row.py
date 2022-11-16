class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        countOccurence = defaultdict(lambda: [0, 0, 0])
        n = len(tops)

        # get the count for top, bottom and both
        for i in range(n):
            if tops[i] == bottoms[i]:
                countOccurence[tops[i]][2] += 1
                continue
            countOccurence[tops[i]][0] += 1
            countOccurence[bottoms[i]][1] += 1

        min_rotation = float('inf')
        for i in range(1, 7):
            if sum(countOccurence[i]) == n:
                return min([countOccurence[i][0], countOccurence[i][1]])

        return -1