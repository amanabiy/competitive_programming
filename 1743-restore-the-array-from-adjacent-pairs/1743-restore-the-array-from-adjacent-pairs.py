class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        ans = []
        visited = set()
        nextNum = defaultdict(list)

        for x, y in adjacentPairs:
            nextNum[x].append(y)
            nextNum[y].append(x)
        

        # find starting point
        for s in nextNum:
            if len(nextNum[s]) == 1:
                ans.append(s)
                break
        
        while ans[-1] not in visited:
            visited.add(ans[-1])
            for val in nextNum[ans[-1]]:
                if val not in visited:
                    ans.append(val)
        
        return ans
        
