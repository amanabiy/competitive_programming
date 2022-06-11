class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        right = 0
        sums = arr[0]
        count = 0
        print(arr)
        while right < len(arr):
            if right - left +1 < k:
                right += 1
                if right < len(arr):
                    sums += arr[right]
            else:
                if sums / k >= threshold:
                    count += 1
                sums -= arr[left]
                left += 1
            
        return count