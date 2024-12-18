class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """
        """
        count = 0
        
        for log in logs:
            if count and log == '../':
                count -= 1
            elif log != './' and log != '../':
                count += 1               
        
        return count