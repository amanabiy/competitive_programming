class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        
        for i in range(len(tickets)):
            ans += min(tickets[i], tickets[k])
            if i == k and tickets[i] == 1:
                break
            if i == k:
                tickets[i] -= 1

        return ans