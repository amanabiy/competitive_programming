class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        totalRefill = 0
        alice = 0
        bob = len(plants) - 1
        currAlice = capacityA
        currBob = capacityB

        while alice <= bob:
            if alice == bob:
                if max(currAlice, currBob) < plants[alice]:
                    totalRefill += 1
                alice += 1
            else:
                if currAlice < plants[alice]:
                    currAlice = capacityA
                    totalRefill += 1
                if currBob < plants[bob]:
                    currBob = capacityB
                    totalRefill += 1
                currAlice -= plants[alice]
                currBob -= plants[bob]
                alice += 1
                bob -= 1
        
        return totalRefill
                    