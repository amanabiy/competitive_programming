class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currSum = sum(arr[:k])
        count = 0
        ans = 0
    
        for i in range(k, len(arr)):
            num = arr[i]
            if (currSum / k) >= threshold:
                ans += 1

            currSum -= arr[i - k]
            currSum += num
            # print("here")
        # print(currSum)
        return ans + 1 if (currSum / k) >= threshold else ans