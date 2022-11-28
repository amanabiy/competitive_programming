class Solution:
    def clumsy(self, n: int) -> int:
        """
        4 * 3 / 2 + 1
        7
        10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
        11 + 7 - 7 + 3 - 2
        12
        """
        nextOp = {
            '*': '//',
            '//': '+',
            '+': '-',
            '-': '*'
        }
        process = [str(n)]
        n -= 1
        currOp = '-'
        
        while n:
            currOp = nextOp[currOp]
            if currOp == '*' or currOp == '//':
                x = process.pop()
                process.append(str(eval(f'{x} {currOp} {n}')))
            else:
                process.append(currOp)
                process.append(str(n))
            n -= 1
        
        return eval(''.join(process))
            
            
            
        