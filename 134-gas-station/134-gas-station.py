class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        i = 0
        prev_cost_sum_remaining = 0
        curr_gas = 0
        index = -1

        for i in range(len(gas)):
            curr_gas += gas[i]
            if curr_gas >= cost[i]:
                index = i if index == -1 else index
                curr_gas -= cost[i]
            else:
                index = -1
                prev_cost_sum_remaining += cost[i] - curr_gas
                curr_gas = 0
            # print(i, prev_cost_sum_remaining, curr_gas, index)
        
        return index if prev_cost_sum_remaining <= curr_gas else -1
        
        