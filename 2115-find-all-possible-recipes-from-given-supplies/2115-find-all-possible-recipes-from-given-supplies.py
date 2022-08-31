class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        """
        graph = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque(supplies)
        ans = []
        
        # build graph and count indegree
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
                indegree[recipes[i]] += 1
        
        while queue:
            sup = queue.popleft()
            for rec in graph[sup]:
                indegree[rec] -= 1
                if indegree[rec] == 0:
                    queue.append(rec)   
                    ans.append(rec)

        return ans