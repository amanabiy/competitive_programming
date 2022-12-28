class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        seen = defaultdict(int)
        mod = 10 ** 9 + 7
        ans = 0
        

        deliciousness.sort()
        for num in deliciousness:
            nextNum = 1 << (num.bit_length())
            if nextNum - num in seen:
                ans = (ans + seen[nextNum - num]) % mod
            if num != 0 and (num - 1) & (num) == 0:
                ans = (ans + seen[0]) % mod            
            seen[num] += 1

        return ans