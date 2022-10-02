class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        total = set([1])
        
        for i in range(2, int(math.sqrt((num))) + 1):
            if num % i == 0:
                total.add(i)
                total.add(num // i)

        return sum(total) == num