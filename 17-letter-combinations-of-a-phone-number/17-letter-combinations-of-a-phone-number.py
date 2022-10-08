class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        ans = []
        
        
        def backtrack(i, collected):
            if i >= len(digits):
                ans.append("".join(collected))
                return

            for letter in letters[int(digits[i])]:
                backtrack(i + 1, collected + [letter])
        
        backtrack(0, [])
        return ans