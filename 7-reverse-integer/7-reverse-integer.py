class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x *= sign
        
        num = 0
        while x:
            num = (num * 10) + (x % 10)
            x //= 10
            # print(num, x)
            if (num > ((2 ** 31) - 1) and sign == 1) or ((num > (2 ** 31)) and sign == -1) :
                num = 0
                break
        
        return num * sign