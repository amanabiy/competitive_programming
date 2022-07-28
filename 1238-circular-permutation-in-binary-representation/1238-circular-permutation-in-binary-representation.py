class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        """
        0   1    2   3   4   5    6  7
        000 001  010 011 100 101 110 111
        
        000 001  011 010 110 111 101 100
        
        3 4 5 6 7 0 1 2
        
        0 1
        0 1 0 1
        00 01 11 10 10 11 01 00
        000 001  011 010 110 111 101 100
    
        """
        ans = deque()
        for i in range(1 << n):
            ans.append(i ^ (i >> 1))
        
        while ans[0] != start:
            popped = ans.popleft()
            ans.append(popped)
        
        return ans