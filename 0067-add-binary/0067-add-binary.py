class Solution:
    def addBinary(self, a: str, b: str) -> str:
        remainder = "0"
        ans = []
        a = a[::-1]
        b = b[::-1]

        for i in range(max(len(a), len(b))):
            first = a[i] if i < len(a) else "0"
            second = b[i] if i < len(b) else "0"
            one = [first, second, remainder]
            if one.count("1") == 3:
                ans.append("1")
                remainder = "1"
            elif one.count("1") == 2:
                ans.append("0")
                remainder = "1"
            elif one.count("1") == 1:
                ans.append("1")
                remainder = "0"
            else:
                ans.append("0")
                remainder = "0"
        
        if remainder == "1":
            ans.append(remainder)
        
        return "".join(reversed(ans))