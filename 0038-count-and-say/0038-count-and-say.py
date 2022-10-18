class Solution:
    def count(self, n: int) -> str:
        if n == 1:
            return ["1"]
        
        ans_lower = self.countAndSay(n - 1)
        
        result = []
        
        count = 1
        for i in range(len(ans_lower) - 1):
            if ans_lower[i] != ans_lower[i + 1]:
                result.extend(list(str(count)))
                result.append(ans_lower[i])
                count = 0
            count += 1

        result.extend(list(str(count)))
        result.append(ans_lower[-1])                

        return result

    def countAndSay(self, n: int) -> str:
        """
        3322251
        23321511
        
        -> countsay(1) -> 1
        -> countsay(2) -> countsay(1) -> "1" -> 11
        -> countsay(3) -> countsay(2) -> "11" -> 21
        -> countsay(4) -> countsay(3) -> "21" -> 1211
        -> countsay(5) -> countsay(4) -> "1211" -> 111221
        
        
        """
        ans = self.count(n)
        return "".join(ans)

        
        