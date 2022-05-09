class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter = ord('a')
        letters = defaultdict(list)
        for i in range(2, 9):
            for j in range(letter, letter+3):
                letters[i].append(chr(j))
            letter += 3
        letters[9] = ['w','x','y','z']
        letters[7].append('s')
        letters[8] = ['t', 'u', 'v']
        
        temp = []
        if digits:
            temp = letters[int(digits[-1])]
            for i in range(len(digits) - 2, -1, -1):
                temp2 = letters[int(digits[i])]
                tempCopy = temp.copy()
                temp = []
                for i in temp2:
                    for j in tempCopy:
                        temp.append("".join([i, j]))      
        return temp
#         def dfs(i, s):
#             if i == len(digits) - 1: return letters[i]
            
            
            