class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        RR.L
        1101
        
        . L . R . . . L R . . L . .
        
        """
        temp = ''
        
        while dominoes != temp:
            temp = dominoes
            dominoes = dominoes.replace('R.L', 'xxx')       # <-- 1)
            dominoes = dominoes.replace('R.', 'RR')         # <-- 2)
            dominoes = dominoes.replace('.L', 'LL')         # <-- 2)

        return  dominoes.replace('xxx', 'R.L')              # <-- 3)
        
            