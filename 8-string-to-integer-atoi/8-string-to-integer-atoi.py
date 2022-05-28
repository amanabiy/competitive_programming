class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        number = 0
        maxNum = 2 ** 31
        sign = 1
        
        if s and (s[0] == "-" or s[0] == "+"):
                sign = -1 if s[0] == "-" else 1
                s = s[1:]
        
        s = s.lstrip("0")
        
        
        for i in range(0, len(s)):
            if s[i].isdigit():
                number = number * 10 + int(s[i])
                if number > maxNum -1 and sign == 1:
                    return maxNum - 1
                if -number < -maxNum:
                    return -maxNum
            else:
                break
        return number * sign
