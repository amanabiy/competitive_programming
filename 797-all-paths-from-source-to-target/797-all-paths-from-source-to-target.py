class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        
        """
        ans = []
        
        def dfs(node, collected):
            if collected[-1] == len(graph) - 1:
                ans.append(collected[::])
                return
            # print(node, collected)
            for nex in graph[node]:
                collected.append(nex)
                dfs(nex, collected)
                collected.pop()
            
        dfs(0, [0])
        return ans