class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        [1, 3, 5]
        [1, 2, 3]
        """
        currSum, ans = 0, 0
        even, odd = 0, 0
        
        for num in arr:
            currSum += num
            if currSum % 2 == 0:
                even += 1
                ans += odd
            else:
                odd += 1
                ans += even + 1
        
        return ans % (10 ** 9 + 7)