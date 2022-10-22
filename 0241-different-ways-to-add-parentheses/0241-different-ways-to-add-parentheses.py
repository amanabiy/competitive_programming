class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        """
              |
        "21-1-1"
        """
        memo = {}
        op = {'+', '-', '*', '/'}
        
        def dp(i, j, memo):
            if j - i + 1<= 2:
                return [int(expression[i:j + 1])]
            
            if (i, j) in memo:
                return memo[(i, j)]

            ans = []
            for x in range(i, j + 1):
    
                if expression[x] in op:
                    left = dp(i, x - 1, memo)
                    right = dp(x + 1, j, memo)
                    for l in left:
                        for r in right:
                            v = eval(f"{l} {expression[x]} {r}")
                            ans.append(v)
                                            
            return ans
        
        return dp(0, len(expression) - 1, {})
            
            