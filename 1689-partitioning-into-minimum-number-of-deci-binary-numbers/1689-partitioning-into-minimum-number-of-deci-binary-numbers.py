class Solution:
    def minPartitions(self, n: str) -> int:
        """
        32
        11
        11
        10
        
        82734
        23478 -> 2
        1256 -> 1
        145 -> 1
        34 -> 3
        1 -> 1
        0
        
        """
        return max(list(n))
            