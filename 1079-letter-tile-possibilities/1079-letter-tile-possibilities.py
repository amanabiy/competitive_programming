class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        visited = set()
        
        
        def backtrack(collected, seen):
            s = ''.join(collected)
            if s not in visited:
                visited.add(s)
            
            for i in range(len(tiles)):
                if i not in seen:
                    seen.add(i)
                    collected.append(tiles[i])
                    backtrack(collected, seen)
                    seen.remove(i)
                    collected.pop()

        backtrack([], set())
        return len(visited) - 1
        