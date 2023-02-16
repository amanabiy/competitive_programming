class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        count = Counter()
        ans = []
        
        for num in changed:
            count[num] += 1
            if num == 0 and count[num] < 2:
                continue
            if num % 2 == 0 and count[num // 2]:
                count[num // 2] -= 1
                count[num] -= 1
                ans.append(num // 2)
        
        if len(ans) == len(changed) / 2:
            return ans
        return []
            
        