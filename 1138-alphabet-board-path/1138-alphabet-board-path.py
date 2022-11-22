class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        letters = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                letters[board[i][j]] = (i, j)
        
        prev = 'a'
        ans = []
        changed = False

        for l in target:
            if prev == 'z' and l != 'z':
                ans.append('U')
                prev = 'u'
            if l == 'z' and prev != 'z':
                changed = True
                l = 'u'
            x1, y1 = letters[prev]
            x2, y2 = letters[l]
            horizontal = x2 - x1
            vertical = y2 - y1
            if horizontal > 0:
                ans += ['D'] * horizontal
            else:
                ans += ['U'] * abs(horizontal)

            if vertical > 0:
                ans += ['R'] * vertical
            else:
                ans += ['L'] * abs(vertical)
                
            prev = l if not changed else 'z'
            if changed:
                ans.append('D')
                changed = False
                
            ans.append('!')
            print(prev)
        
        return ''.join(ans)
                