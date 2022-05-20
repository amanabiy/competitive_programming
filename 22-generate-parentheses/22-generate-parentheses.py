class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        (()())
        (())
        
        010101
        000111
        
        
        """
        ans = []
        
        def build(op, cl, strs):
            if op == cl == 0:
                ans.append("".join(strs))
                return
            if op > 0:
                strs.append("(")
                build(op -1, cl, strs)
                strs.pop()
            if op < cl:
                strs.append(")")
                build(op, cl - 1, strs)
                strs.pop()
        
        build(n,n, [])
        return ans