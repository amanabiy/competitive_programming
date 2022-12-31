class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        def check(word):
            for i in range(len(word) - 1):
                if pattern[i] == 'I':
                    if word[i] > word[i + 1]:
                        return False
                if pattern[i] == 'D':
                    if word[i] < word[i + 1]:
                        return False
            return True
        
        ans = [[]]
        def backtrack(a, visited):
            if len(a) == len(pattern) + 1:
                if check(''.join(a)):
                    ans[0] = a[::]
                    return True
                return False
            
            for i in range(1, 10):
                if i not in visited:
                    a.append(str(i))
                    visited.add(i)
                    if backtrack(a, visited):
                        return True
                    a.pop()
                    visited.remove(i)
            
            return False
        
        backtrack([], set())
        return ''.join(ans[0])