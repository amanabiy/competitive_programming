class Solution: 
    def kIncreasing(self, arr: List[int], k: int) -> int:
        ans = 0
        
        for j in range(k):
            collect = []
            count = 0
            for i in range(j, len(arr), k):
                num = arr[i]
                if not collect or collect[-1] <= num:
                    collect.append(num)
                else:
                    left = 0
                    right = len(collect) - 1
                    index = bisect.bisect_right(collect, num)
                    collect[index] = num
                count += 1
            ans += count - len(collect)
        
        return ans