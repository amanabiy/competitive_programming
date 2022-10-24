class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """
        ["un","iq","ue"]
        """
        
        bitArr = []
        
        for i, word in enumerate(arr):
            bitValue = 0
            for chrs in word:
                v = 1 << (ord(chrs) - ord('a') + 1)
                if v & bitValue:
                    arr[i] = ""
                    bitValue = 0
                    break
                bitValue |= v
            bitArr.append(bitValue)
        
        def dfs(i, prev, arr, bitArr, memo = {}):
            if i >= len(arr):
                return 0

            take = not_take = 0
            if (i, prev) not in memo:
                if bitArr[i] & prev == 0:
                    take = dfs(i + 1, prev | bitArr[i], arr, bitArr, memo) + len(arr[i])
                not_take = dfs(i + 1, prev, arr, bitArr, memo)

                memo[(i, prev)] = max(take, not_take)
            return memo[(i, prev)]
        
        return dfs(0, 0, arr, bitArr)
            