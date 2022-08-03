class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for letter in s:
            if letter == ']':
                word = []
                
                while stack and stack[-1] != ['[']:
                    word += stack.pop()
                
                stack.pop()
                num = ""

                while stack and '0' <= stack[-1][0] <= '9':
                    num += stack.pop()[0]
                    
                stack.append(word * int(num[::-1]))
                
            else:
                stack.append([letter])
        
        ans = []
        
        for sequence in stack:
            ans += sequence[::-1]

        return ''.join(ans)
                