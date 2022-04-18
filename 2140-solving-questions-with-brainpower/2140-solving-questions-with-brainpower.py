class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = defaultdict(int)
        
        for i in range(len(questions) - 1, -1 , -1):
            memo[i] = max(questions[i][0] + memo[i + questions[i][1] + 1], memo[i+1])      

        return max(memo.values())
