class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        """
        4 -2 2 -4
        0 1 2 3
        -4 -2 2 4
        
        arr[2 * i + 1] == 2 * arr[2 * i]
        """
        count = Counter(arr)
        # print(sorted(arr, key = lambda x: abs(x)))
        for num in sorted(arr, key = lambda x: abs(x)) :
            if count[num] == 0:
                continue
            if count[2 * num] == 0:
                return False
            count[num] -= 1
            count[2 * num] -= 1

        return True