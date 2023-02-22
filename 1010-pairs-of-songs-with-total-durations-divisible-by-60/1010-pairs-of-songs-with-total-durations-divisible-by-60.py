class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder = Counter()
        ans = 0

        for i in time:
            if i % 60 != 0:
                ans += remainder[60 - (i % 60)]
            else:
                ans += remainder[0]
            remainder[i % 60] += 1

        return ans
        
        