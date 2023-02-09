class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        swapped = False

        for j in range(len(num)):
            swap = j

            for i in range(j + 1, len(num)):
                if swap == j and num[swap] == num[i]:
                    continue
                if num[swap] <= num[i]:
                    swap = i
                    swapped = True

            if swapped:
                num[j], num[swap] = num[swap], num[j]
                break

        return int(''.join(num))
        
        