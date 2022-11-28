class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        ans = 0
        
        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)
        
        nodes = []
        for i in range(n):
            nodes.append((len(graph[i]), i))
        
        v = n
        nodes.sort(reverse=True)
        for size, i in nodes:
            ans += size * v
            v -= 1
        
        return ans