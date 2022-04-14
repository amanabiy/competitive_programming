class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ing = {}
        graph = defaultdict(list)
        sup = set(supplies)
        queue = deque()
        ans = []
        
        for rec, ingd in zip(recipes, ingredients):
            ing[rec] = len(ingd)
        
        for i in range(len(recipes)):
            for inds in ingredients[i]:
                graph[inds].append(recipes[i])
        
        
        queue.extend(supplies)
        
        while queue:
            node = queue.popleft()
            if node not in sup:
                ans.append(node)
            for val in graph[node]:
                ing[val] -= 1
                if ing[val] == 0:
                    queue.append(val)
                    
        return ans
        
        