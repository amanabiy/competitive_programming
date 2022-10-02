class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        for one die with the max k I will only be able to reach the targets from 1 to 30
          1 2 3 ... 30 0 0 0 ... 1000
        k = 6 and n = 1 and taret = 3
         1 2 3 4 5 6 7   Faces: 1 2 3 4 5 6     n = 2  target = 1 - 1
                                                       target = 2 -> 1 + 1 and 2
                                                       target = 3 -> 1 + 2 and 2 + 1
        inf = -inf
           0     1   2    3   4   5   6   7
        0  0    inf inf inf  inf inf inf inf
        1  inf   1   1    1   1   1   1   inf
        2  inf   1   1   
        
        1 + 1
        2 + 0
        
        
        
        roll - 1 -> 7 - 1 = 6
        roll - 1 -> 2 - 1 = 1
        I can reach 1 only in one way
        I can reach 2 for each die I will check the previous sum that would allow me to reach the current sum
        curr - rolledDie = previousSum
        if I can get the the number of ways I could reach previousSum I can easliy get the number of ways I could reach that sum if I rolled that dice so I can add it to the number of ways I can reach currently
        
        1 -> add one on zero or take the max way I could reach one)
        2 -> add one from the previous roll and one from the current roll)
        3 -> add one from the previous two and 2 from current roll, or add one from the previous 2 and 1 from the current two
                
                prev + curr
        4 -> max(1 + 3, 3 + 1, 2 + 2) -> add the number of ways and take maximum

       
        """
        
        dp = [ [0 for _ in range(target + 1)] for _ in range(n + 1) ]
        dp[0][0] = 1
        # print(dp)
        
        for trial in range (1, n + 1):
            for num in range (1, target + 1):
                
                # calculate from which previous some to inherit from
                for face in range(1, k + 1):
                    prev = num - face

                    # look it up in the previous and add one and take the maximum
                    if prev >= 0:
                        dp[trial][num] += dp[trial - 1][prev]

        return dp[-1][-1] % (10 ** 9 + 7)
                