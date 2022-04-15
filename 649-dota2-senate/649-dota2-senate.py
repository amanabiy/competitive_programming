class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R_que = deque()
        D_que = deque()
        
        for i in range(len(senate)):
            if senate[i] == "R":
                R_que.append(i)
            else:
                D_que.append(i)
        
        while R_que and D_que:
            curr_r = R_que.popleft()
            curr_d = D_que.popleft()
            
            if curr_r < curr_d:
                R_que.append(curr_r + len(senate))
            else:
                D_que.append(curr_d + len(senate))
        
        return "Radiant" if R_que else "Dire"