class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
    
        while target != 1:
            if target % 2 == 0 and maxDoubles:
                maxDoubles -= 1
                target //= 2
            elif not maxDoubles:
                count += target - 2
                target = 1
            else:
                target -= 1
            count += 1
            
        return count