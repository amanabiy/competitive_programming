class Solution:
    def numberOfWays(self, s: str) -> int:
        ans = 0
        n = len(s)
        countOnesLeftRight = [0]
        countOnesRightLeft = [0]
        
        count = 0
        c = 0
        for i in range(n):
            count += int(s[i])
            r = n - i - 1
            c += int(s[r])
            countOnesLeftRight.append(count)
            countOnesRightLeft.append(c)
        
        countOnesRightLeft = countOnesRightLeft[::-1]
        
        for i in range(n):
            if s[i] == '0':
                ans += countOnesRightLeft[i + 1] * countOnesLeftRight[i]
            else:
                leftZero = i - countOnesLeftRight[i]
                rightZero = n - i - 1 - countOnesRightLeft[i + 1]
                ans +=leftZero * rightZero
        
        return ans