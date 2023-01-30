class Solution:
    def tribonacci(self, n: int) -> int:
        """
        0 1 2 3 4
        0 1 1 2 4
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1
        one = 0
        two = 1
        three = 1
        curr = 2
        while curr < n:
            one, two, three = two, three, one + two + three
            curr += 1
        return three