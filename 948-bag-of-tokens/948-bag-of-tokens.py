class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """
        100 200 300 400
            500      |
        score = 0
        """
        
        toScore = 0
        toToken = len(tokens)
        tokens.sort()
        maxScore = 0
        curr_score = 0
        
        while toScore < toToken and (tokens[toScore] <= power or curr_score > 0):
            if tokens[toScore] <= power:
                power -= tokens[toScore]
                toScore += 1
                curr_score += 1
                maxScore = max(maxScore, curr_score)
            else:
                curr_score -= 1
                toToken -= 1
                power += tokens[toToken]
        
        return maxScore