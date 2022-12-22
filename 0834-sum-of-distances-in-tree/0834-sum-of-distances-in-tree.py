class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        memo = {}
        answer = [0] * n
        graph = defaultdict(list)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node, parent):
            ans = [0, 1]
            for child in graph[node]:
                if child != parent:
                    t = dfs(child, node)
                    ans[0] += t[0]
                    ans[1] += t[1]
            memo[node] = ans[::]
            ans[0] += ans[1]
            return ans

        def getTotalAns(node, parent, answer):
            if parent != -1:
                answer[node] = answer[parent] - memo[node][1] + (n - memo[node][1])

            for child in graph[node]:
                if child != parent:
                    getTotalAns(child, node, answer)

        dfs(0, -1)
        answer[0] = memo[0][0]
        getTotalAns(0, -1, answer)

        return answer
        
