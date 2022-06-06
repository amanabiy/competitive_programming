class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        """
        get fibonacci numbers less than 7
        1, 2, 3, 5
        """
        fibonaci = [1, 1]
        
        while True:
            val = fibonaci[-1] + fibonaci[-2]
            if val > k:
                break
            fibonaci.append(val)
        count = 0
        
        while k:
            div = k // fibonaci[-1]
            k -= (fibonaci[-1] * div)
            count += 1 * div
            fibonaci.pop()
        
        return count