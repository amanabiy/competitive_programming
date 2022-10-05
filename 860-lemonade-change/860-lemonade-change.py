class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        
        """
        coins = defaultdict(int)
        
        for bill in bills:
            if bill == 10:
                if coins[5] <= 0:
                    return False
                coins[5] -= 1
            elif bill == 20:
                if (coins[5] <= 0) or (coins[10] <= 0 and coins[5] <= 2) :
                    return False
                if coins[10]:
                    coins[10] -= 1
                    coins[5] -= 1
                else:
                    coins[5] -= 3

            coins[bill] += 1
        
        return True