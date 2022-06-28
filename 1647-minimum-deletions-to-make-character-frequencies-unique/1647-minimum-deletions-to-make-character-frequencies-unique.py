class Solution:
    def minDeletions(self, s: str) -> int:
        """
        sort the string with count decreasing count
        aaabbbcc
        (3,2,1)
        
        """
        countLetter = Counter(s)
        visited = set()
        deleted = 0
        
        for key, value in sorted(countLetter.items(), key=lambda x: x[1]):
            while value in visited and value != 0:
                value -= 1
                deleted += 1
            visited.add(value)
        
        return deleted