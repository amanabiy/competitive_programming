class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = defaultdict(int)
        
        for froms, to in edges:
            incoming[to] += 1

        return [key for key in range(n) if incoming[key] == 0]
        