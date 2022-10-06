class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []
        while a > 0 or b > 0:
            if a > b:
                ans.append('a' * (a if a == 1 else 2))
                if b:
                    ans.append('b')
                    b -= 1
                a -= 2
                # else:
                #     ans.append('b')
                #     ans.append('a' * 2)
            elif a < b:
                # if ans and ans[-1] == '':
                ans.append('b' * (b if b == 1 else 2))
                if a:
                    ans.append('a')
                    a -= 1
                b -= 2
                # else:
                #     ans.append('b')
                #     ans.append('a' * 2)
            
            else:
                if a >= 2:
                    if ans and ans[-1][-1] == 'a':
                        ans.append('bbaa')
                    else:
                        ans.append('aabb')
                else:
                    if ans and ans[-1][-1] == 'a':
                        ans.append('ba')
                    else:
                        ans.append('ab')
                a -= 2
                b -= 2
        
        return ''.join(ans)
                